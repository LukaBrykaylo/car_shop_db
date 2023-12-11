USE bdlab4;

DROP PROCEDURE IF EXISTS insert_into_chassis;
DELIMITER //
CREATE PROCEDURE insert_into_chassis (
  IN chassis_model VARCHAR(45),
  IN chassis_wheel_number INT
)
BEGIN
  INSERT INTO `bdlab4`.`chassis` (`model`, `wheel_number`)
  VALUES (chassis_model, chassis_wheel_number);
END //
DELIMITER ;
-- ================================================================================================

DROP PROCEDURE IF EXISTS insert_into_order_car_with_checks;
DELIMITER //
CREATE PROCEDURE insert_into_order_car_with_checks (
  IN order_id INT,
  IN car_length INT,
  IN car_width INT,
  IN car_engine_id INT,
  IN car_body_id INT,
  IN car_body_type VARCHAR(45),
  IN car_chassis_id INT,
  IN car_drive_id INT,
  IN car_photo_id INT,
  IN car_model_id INT
)
BEGIN
    INSERT INTO `bdlab4`.`order_has_car` (`order_id`, `car_id`)
    VALUES (
      order_id,
      (SELECT `id` FROM `bdlab4`.`car`
       WHERE `length` = car_length
       AND `width` = car_width
       AND `engine_id` = car_engine_id
       AND `body_id` = car_body_id
       AND `body_body_type` = car_body_type
       AND `chassis_id` = car_chassis_id
       AND `drive_id` = car_drive_id
       AND `photo_id` = car_photo_id
       AND `model_id` = car_model_id)
    );
END //
DELIMITER ;
-- ================================================================================================

DROP PROCEDURE IF EXISTS insert_10_into_photo;
DELIMITER //
CREATE PROCEDURE insert_10_into_photo ()
BEGIN
DECLARE i INT DEFAULT 1;
DECLARE image VARCHAR(30);
  WHILE i <= 10 DO
    SET image = CONCAT('Image', i);
    INSERT INTO `bdlab4`.`photo` (`image`)
    VALUES (
      image
    );
	SET i = i + 1;
  END WHILE;
END //
DELIMITER ;
-- ================================================================================================

DROP FUNCTION IF EXISTS get_comment_value;
DELIMITER //
CREATE FUNCTION get_comment_value(
  type_of VARCHAR(15)
)
RETURNS INT
DETERMINISTIC
BEGIN
  DECLARE result INT DEFAULT 0;

  IF type_of = 'MAX' THEN
	SELECT MAX(`rate`) INTO result FROM `comment`;
  ELSEIF type_of = 'MIN' THEN
	SELECT MIN(`rate`) INTO result FROM `comment`;
  ELSEIF type_of = 'AVG' THEN
	SELECT AVG(`rate`) INTO result FROM `comment`;
  ELSEIF type_of = 'SUM' THEN
	SELECT SUM(`rate`) INTO result FROM `comment`;
  END IF;

  RETURN result;
END //
DELIMITER ;
-- ====
DROP PROCEDURE IF EXISTS call_get_comment_value;
DELIMITER //
CREATE PROCEDURE call_get_comment_value(
  IN type_of VARCHAR(15)
)
BEGIN
  DECLARE result INT;

  SET result = get_comment_value(type_of);

  SELECT CONCAT('The ', type_of, ' value of rate is: ', result) AS result_message;
END //
DELIMITER ;
-- ================================================================================================

DROP PROCEDURE IF EXISTS dynamic_table;
DELIMITER //
CREATE PROCEDURE dynamic_table()
BEGIN
    DECLARE done INT DEFAULT 0;
    DECLARE tableName VARCHAR(255);
    DECLARE columnName VARCHAR(255);
    DECLARE columnType VARCHAR(45);
    DECLARE numColumns INT;

    DECLARE cur CURSOR FOR
        SELECT COLUMN_NAME, DATA_TYPE
        FROM INFORMATION_SCHEMA.COLUMNS
        WHERE TABLE_NAME = 'engine' AND COLUMN_NAME NOT IN ('id', 'name');
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = 1;
    OPEN cur;
    read_loop: LOOP
        FETCH cur INTO columnName, columnType;
        IF done THEN
            LEAVE read_loop;
        END IF;
        SET numColumns = FLOOR(RAND() * 9);
        SET tableName = CONCAT(columnName, '_', REPLACE(REPLACE(REPLACE(CAST(NOW() AS CHAR), '-', '_'), ' ', '_'), ':', '_'));
        SET @sql = CONCAT('CREATE TABLE ', tableName, ' (id INT NOT NULL AUTO_INCREMENT, ');
        SET @i = 1;
        WHILE @i <= numColumns DO
            SET @sql = CONCAT(@sql, 'column', @i, ' ', columnType);
            SET @i = @i + 1;
            IF @i <= numColumns THEN
                SET @sql = CONCAT(@sql, ', ');
            END IF;
        END WHILE;
        SET @sql = CONCAT(@sql, ', PRIMARY KEY (id)) ENGINE = InnoDB;');
        PREPARE stmt FROM @sql;
        EXECUTE stmt;
        DEALLOCATE PREPARE stmt;
    END LOOP;
    CLOSE cur;
END //
DELIMITER ;