-- MySQL Script generated by MySQL Workbench
-- Sat Feb 13 01:28:44 2021
-- Model: New Model    Version: 1.0
-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mp
-- -----------------------------------------------------
-- База данных врачей, медицинских карт и медикаментов.

-- -----------------------------------------------------
-- Schema mp
--
-- База данных врачей, медицинских карт и медикаментов.
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `mp` DEFAULT CHARACTER SET utf8 COLLATE utf8_bin ;
USE `mp` ;

-- -----------------------------------------------------
-- Table `mp`.`users`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mp`.`users` (
  `iduser` INT NOT NULL AUTO_INCREMENT COMMENT 'ID врача',
  `email` VARCHAR(64) NOT NULL COMMENT 'Почта',
  `password` VARCHAR(255) NOT NULL COMMENT 'Пароль',
  `paid_before` DATE NOT NULL DEFAULT DATE_ADD(CURDATE(), INTERVAL +3 DAY) COMMENT 'Оплачен доступ до ',
  `registered_at` DATE NOT NULL DEFAULT CURDATE() COMMENT 'Дата регистрации',
  `verification_text` VARCHAR(20) NULL COMMENT 'Текст, генерируемый для верификации по почте действий пользователя.',
  PRIMARY KEY (`iduser`))
ENGINE = InnoDB
COMMENT = 'Пользователи (врачи)';


-- -----------------------------------------------------
-- Table `mp`.`cards`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mp`.`cards` (
  `idcard` INT NOT NULL AUTO_INCREMENT COMMENT 'ID карты',
  `iduser` INT NOT NULL COMMENT 'ID врача',
  `date` DATE NOT NULL DEFAULT NOW() COMMENT 'Дата вызова',
  `order` VARCHAR(64) NOT NULL COMMENT 'Номер наряда',
  `status` SET("draft", "ready", "archive", "template") NOT NULL DEFAULT 'draft' COMMENT 'Статус карты (черновик, завершена, архивная, шаблон)',
  `comment` VARCHAR(45) NULL COMMENT 'Комментарий',
  PRIMARY KEY (`idcard`),
  INDEX `fk_cards_users_idx` (`iduser` ASC),
  CONSTRAINT `fk_cards_users`
    FOREIGN KEY (`iduser`)
    REFERENCES `mp`.`users` (`iduser`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
COMMENT = 'Медицинские карты (листы осмотра)';


-- -----------------------------------------------------
-- Table `mp`.`medicaments`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mp`.`medicaments` (
  `idmedicament` INT NOT NULL AUTO_INCREMENT COMMENT 'ID медикамента',
  `title` VARCHAR(64) NOT NULL COMMENT 'Название',
  `added_at` DATE NOT NULL DEFAULT CURDATE() COMMENT 'Дата добавления',
  `group` VARCHAR(32) NULL COMMENT 'Категория',
  `added_by_user` INT NOT NULL COMMENT 'Добавивший врач',
  PRIMARY KEY (`idmedicament`),
  INDEX `fk_medicaments_users1_idx` (`added_by_user` ASC),
  CONSTRAINT `fk_medicaments_users1`
    FOREIGN KEY (`added_by_user`)
    REFERENCES `mp`.`users` (`iduser`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
COMMENT = 'Медицинские препараты';


-- -----------------------------------------------------
-- Table `mp`.`recipes`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mp`.`recipes` (
  `iduser` INT NOT NULL COMMENT 'ID врача',
  `idmedicament` INT NOT NULL COMMENT 'ID медикамента',
  `count` INT NOT NULL COMMENT 'число используемых\n',
  PRIMARY KEY (`iduser`, `idmedicament`),
  INDEX `fk_users_has_medicaments_medicaments1_idx` (`idmedicament` ASC),
  INDEX `fk_users_has_medicaments_users1_idx` (`iduser` ASC),
  CONSTRAINT `fk_users_has_medicaments_users1`
    FOREIGN KEY (`iduser`)
    REFERENCES `mp`.`users` (`iduser`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_users_has_medicaments_medicaments1`
    FOREIGN KEY (`idmedicament`)
    REFERENCES `mp`.`medicaments` (`idmedicament`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
COMMENT = 'Выписанные врачом медикменты (рецепты)';


-- -----------------------------------------------------
-- Table `mp`.`texts`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mp`.`texts` (
  `idtext` INT NOT NULL AUTO_INCREMENT COMMENT 'ID текста\n',
  `content` VARCHAR(128) NOT NULL COMMENT 'Текст для ввода',
  `input` VARCHAR(32) NOT NULL COMMENT 'Поле ввода текста\n',
  `iduser` INT NOT NULL COMMENT 'Пользователь\n',
  `count` INT NOT NULL DEFAULT 1,
  PRIMARY KEY (`idtext`),
  INDEX `fk_texts_users1_idx` (`iduser` ASC),
  CONSTRAINT `fk_texts_users1`
    FOREIGN KEY (`iduser`)
    REFERENCES `mp`.`users` (`iduser`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
COMMENT = 'Тексты';


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
