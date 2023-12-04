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

