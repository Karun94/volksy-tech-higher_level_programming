-- create db and table like cities
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE cities(id INT AUTO_INCREMENT NOT NULL PRIMARY KEY, state_id INT NOT NULL FOREIGN KEY, name VARCHAR(256) NOT NULL, REFERENCES states(id));
