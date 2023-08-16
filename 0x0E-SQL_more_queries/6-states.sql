-- Script creates database hbtn_0d_usa

-- Creates the database
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Using the database
USE hbtn_0d_usa;

-- Creates table states if not existing
CREATE TABLE IF NOT EXISTS states (
    id INT AUTO_INCREMENT UNIQUE NOT NULL PRIMARY KEY,
    name VARCHAR(256) NOT NULL
    );