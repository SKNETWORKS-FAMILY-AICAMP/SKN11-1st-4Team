CREATE DATABASE IF NOT EXISTS green_car;
USE green_car;

DROP TABLE IF EXISTS charger_type;
DROP TABLE IF EXISTS region;
DROP TABLE IF EXISTS regional_charger_count;
DROP TABLE IF EXISTS regional_entire_car_count;
DROP TABLE IF EXISTS regional_eco_car_count;


CREATE TABLE charger_type (
    charger_key INT PRIMARY KEY AUTO_INCREMENT,
    fuel_type VARCHAR(255) NOT NULL,
    charging_speed VARCHAR(255) -- 완속, 급속, null이면 수소
)ENGINE=INNODB;

CREATE TABLE region(
    region_key INT PRIMARY KEY AUTO_INCREMENT, -- files 폴더에 있는 eco_registration에 있는 서울 부산 대구... 제주 순으로 region_key가 1부터 17까지 부여됨
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


CREATE TABLE regional_car_count(
    region_key INT,
    fuel_type VARCHAR(255) NOT NULL, -- elec, hydro, hybrid from eco-car-registration // others from 지표서비스
    car_count INT,
    car_count_date DATE,
    PRIMARY KEY(region_key, fuel_type, car_count_date),
    FOREIGN KEY(region_key) REFERENCES region(region_key)
)ENGINE=INNODB;

