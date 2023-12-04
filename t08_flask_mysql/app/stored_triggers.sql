USE bdlab4;

DROP TRIGGER IF EXISTS before_insert_car;

DELIMITER //
CREATE TRIGGER before_insert_car
BEFORE INSERT ON `bdlab4`.`car`
FOR EACH ROW
BEGIN
  DECLARE model_count INT;

  SELECT COUNT(*) INTO model_count FROM `bdlab4`.`model` WHERE `id` = NEW.`model_id`;

  IF model_count = 0 THEN
    SIGNAL SQLSTATE '45000'
    SET MESSAGE_TEXT = 'Model does not exist';
  END IF;
END //
DELIMITER ;
-- ================================================================================================

DROP TRIGGER IF EXISTS check_no_two_zeros;
DELIMITER //
CREATE TRIGGER check_no_two_zeros
BEFORE INSERT ON `model`
FOR EACH ROW
BEGIN
  DECLARE last_two_chars VARCHAR(2);
  SET last_two_chars = RIGHT(NEW.`model_name`, 2);
  IF last_two_chars = '00' THEN
    SIGNAL SQLSTATE '45000'
    SET MESSAGE_TEXT = 'Error: Value cannot end with two zeros.';
  END IF;
END //
DELIMITER ;
-- ================================================================================================

DROP TRIGGER IF EXISTS allowed_clients_names;
DELIMITER //
CREATE TRIGGER allowed_clients_names
BEFORE INSERT ON `client`
FOR EACH ROW
BEGIN
  DECLARE allowed_names VARCHAR(90);

  SET allowed_names = 'Svitlana,Petro,Olha,Taras';

  IF FIND_IN_SET(NEW.`name`, allowed_names) = 0 THEN
    SIGNAL SQLSTATE '45000'
    SET MESSAGE_TEXT = 'Error: Invalid name. Allowed names are Svitlana, Petro, Olha, Taras.';
  END IF;
END //
DELIMITER ;
-- ================================================================================================

DROP TRIGGER IF EXISTS check_input_format;
DELIMITER //
CREATE TRIGGER check_input_format
BEFORE INSERT ON `engine`
FOR EACH ROW
BEGIN
  DECLARE input_value VARCHAR(45);
  SET input_value = NEW.`name`;
  IF NOT (input_value REGEXP '^[A-LN-QS-Z]{2}-[0-9]{3}-[0-9]{2}$') THEN
    SIGNAL SQLSTATE '45000'
    SET MESSAGE_TEXT = 'Error: Invalid format for your_column.';
  END IF;
END //
DELIMITER ;