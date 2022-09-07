--  a script that lists all records of the table second_table of the database greater than or equal to 10
-- Sorts and displays the records
SELECT `score`, `name` FROM second_table
    WHERE `score` >= 10
    ORDER BY `score` DESC;
