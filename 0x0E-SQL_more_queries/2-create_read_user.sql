-- script to create database
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- Creates user 
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';

-- Grants select permission
GRANT SELECT ON hbtn_od_2.* TO 'user_0d_2'@'localhost';

-- Apply changes
FLUSH PRIVILEGES;