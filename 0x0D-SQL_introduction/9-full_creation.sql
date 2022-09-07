-- a script that creates a table second_table in the database
-- Creates table
CREATE TABLE IF NOT EXISTS second_table
(
    id INT,
    name VARCHAR(256),
    score INT
);

-- Creates a row
INSERT INTO second_table
    VALUES (1, 'John', 10);

-- Creates a row
INSERT INTO second_table
    VALUES (2, 'Alex', 3);

-- Creates a row
INSERT INTO second_table
    VALUES (3, 'Bob', 14);

-- Creates a row
INSERT INTO second_table
    VALUES (4, 'George', 8);
