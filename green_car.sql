CREATE DATABASE green_car;
USE green_car;



CREATE TABLE charger_type (
    charger_key INT PRIMARY KEY AUTO_INCREMENT,
    fuel_type VARCHAR(255) NOT NULL,
    charging_speed VARCHAR(255) -- 완속, 급속, null이면 수소
)ENGINE=INNODB;

CREATE TABLE region(
    region_key INT PRIMARY KEY AUTO_INCREMENT,
    region_name VARCHAR(255) NOT NULL
)ENGINE=INNODB;

CREATE TABLE regional_charger_count(
    region_key INT,
    charger_key INT,
    charger_count INT,
    charger_count_date DATE,
    PRIMARY KEY(region_key, charger_key, charger_count_date),
    FOREIGN KEY(region_key) REFERENCES region(region_key),
    FOREIGN KEY(charger_key) REFERENCES charger_type(charger_key)
)ENGINE=INNODB;

CREATE TABLE regional_entire_car_count(
    -- TODO; 연료별 자동차 긁어오기
)

CREATE TABLE regional_eco_car_count(
    region_key INT,
    fuel_type VARCHAR(255) NOT NULL,
    car_count INT,
    car_count_date DATE,
    PRIMARY KEY(region_key, fuel_type, car_count_date),
    FOREIGN KEY(region_key) REFERENCES region(region_key)
)ENGINE=INNODB;


