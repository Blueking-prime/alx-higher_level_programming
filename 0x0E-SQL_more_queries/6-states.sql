-- a script that creates the database hbtn_0d_usa and the table states (in the database hbtn_0d_usa)
-- Create database
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Select database
USE hbtn_0d_usa;

-- Create table
CREATE TABLE IF NOT EXISTS states (
    PRIMARY KEY(id),
    id   INT                    AUTO_INCREMENT,
    name VARCHAR(256) NOT NULL
);
