SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema bdlab4
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `bdlab4` DEFAULT CHARACTER SET utf8 ;
USE `bdlab4` ;

-- -----------------------------------------------------
-- Table `bdlab4`.`engine`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `bdlab4`.`engine` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NOT NULL,
  `horse_power` INT NOT NULL,
  `max_speed` INT NOT NULL,
  `manual` TINYINT NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `bdlab4`.`body`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `bdlab4`.`body` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `body_type` VARCHAR(45) NOT NULL,
  `seats` INT NOT NULL,
  `color` VARCHAR(45) NOT NULL,
  `is_leather` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id`, `body_type`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `bdlab4`.`chassis`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `bdlab4`.`chassis` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `model` VARCHAR(45) NOT NULL,
  `wheel_number` INT NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `bdlab4`.`drive`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `bdlab4`.`drive` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `is_4WD` TINYINT NOT NULL,
  `wheel_number` INT NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `bdlab4`.`photo`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `bdlab4`.`photo` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `image` VARCHAR(30) NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `bdlab4`.`model`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `bdlab4`.`model` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `model_name` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `bdlab4`.`car`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `bdlab4`.`car` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `length` INT NOT NULL,
  `width` INT NOT NULL,
  `engine_id` INT NOT NULL,
  `body_id` INT NOT NULL,
  `body_body_type` VARCHAR(45) NOT NULL,
  `chassis_id` INT NOT NULL,
  `drive_id` INT NOT NULL,
  `photo_id` INT NOT NULL,
  `model_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_car_engine1_idx` (`engine_id` ASC) VISIBLE,
  INDEX `fk_car_body1_idx` (`body_id` ASC, `body_body_type` ASC) VISIBLE,
  INDEX `fk_car_chassis1_idx` (`chassis_id` ASC) VISIBLE,
  INDEX `fk_car_drive1_idx` (`drive_id` ASC) VISIBLE,
  INDEX `fk_car_photo1_idx` (`photo_id` ASC) VISIBLE,
  INDEX `fk_car_model1_idx` (`model_id` ASC) VISIBLE,
  CONSTRAINT `fk_car_engine1`
    FOREIGN KEY (`engine_id`)
    REFERENCES `bdlab4`.`engine` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_car_body1`
    FOREIGN KEY (`body_id` , `body_body_type`)
    REFERENCES `bdlab4`.`body` (`id` , `body_type`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_car_chassis1`
    FOREIGN KEY (`chassis_id`)
    REFERENCES `bdlab4`.`chassis` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_car_drive1`
    FOREIGN KEY (`drive_id`)
    REFERENCES `bdlab4`.`drive` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_car_photo1`
    FOREIGN KEY (`photo_id`)
    REFERENCES `bdlab4`.`photo` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_car_model1`
    FOREIGN KEY (`model_id`)
    REFERENCES `bdlab4`.`model` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `bdlab4`.`city`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `bdlab4`.`city` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(50) NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `bdlab4`.`comment`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `bdlab4`.`comment` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NULL,
  `comment_text` VARCHAR(300) NOT NULL,
  `rate` INT NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `bdlab4`.`shop`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `bdlab4`.`shop` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `cars_number` INT NOT NULL,
  `street_address` VARCHAR(45) NOT NULL,
  `phone` DECIMAL NOT NULL,
  `city_id` INT NOT NULL,
  `comment_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_shop_city1_idx` (`city_id` ASC) VISIBLE,
  INDEX `fk_shop_comment1_idx` (`comment_id` ASC) VISIBLE,
  UNIQUE INDEX `phone_UNIQUE` (`phone` ASC) VISIBLE,
  CONSTRAINT `fk_shop_city1`
    FOREIGN KEY (`city_id`)
    REFERENCES `bdlab4`.`city` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_shop_comment1`
    FOREIGN KEY (`comment_id`)
    REFERENCES `bdlab4`.`comment` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `bdlab4`.`client`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `bdlab4`.`client` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NOT NULL,
  `surname` VARCHAR(45) NOT NULL,
  `phone` DECIMAL NOT NULL,
  `age` INT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `bdlab4`.`order`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `bdlab4`.`order` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `client_id` INT NOT NULL,
  `shop_id` INT NOT NULL,
  `order_time` DATE NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_order_client1_idx` (`client_id` ASC) VISIBLE,
  INDEX `fk_order_shop1_idx` (`shop_id` ASC) VISIBLE,
  CONSTRAINT `fk_order_client1`
    FOREIGN KEY (`client_id`)
    REFERENCES `bdlab4`.`client` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_order_shop1`
    FOREIGN KEY (`shop_id`)
    REFERENCES `bdlab4`.`shop` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `bdlab4`.`order_car`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `bdlab4`.`order_car` (
  `order_id` INT NOT NULL,
  `car_id` INT NOT NULL,
  `number` INT NOT NULL,
  PRIMARY KEY (`order_id`, `car_id`),
  INDEX `fk_order_has_car_car1_idx` (`car_id` ASC) VISIBLE,
  INDEX `fk_order_has_car_order1_idx` (`order_id` ASC) VISIBLE,
  CONSTRAINT `fk_order_has_car_order1`
    FOREIGN KEY (`order_id`)
    REFERENCES `bdlab4`.`order` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_order_has_car_car1`
    FOREIGN KEY (`car_id`)
    REFERENCES `bdlab4`.`car` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `bdlab4`.`test_drive`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `bdlab4`.`test_drive` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `client_id` INT NOT NULL,
  `car_id` INT NOT NULL,
  `comment_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_test_drive_client1_idx` (`client_id` ASC) VISIBLE,
  INDEX `fk_test_drive_car1_idx` (`car_id` ASC) VISIBLE,
  INDEX `fk_test_drive_comment1_idx` (`comment_id` ASC) VISIBLE,
  CONSTRAINT `fk_test_drive_client1`
    FOREIGN KEY (`client_id`)
    REFERENCES `bdlab4`.`client` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_test_drive_car1`
    FOREIGN KEY (`car_id`)
    REFERENCES `bdlab4`.`car` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_test_drive_comment1`
    FOREIGN KEY (`comment_id`)
    REFERENCES `bdlab4`.`comment` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;