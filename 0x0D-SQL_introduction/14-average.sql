-- a script that computes the score average of all records in the table second_table of the database
-- Display average
SELECT SUM(`score`) / COUNT(`score`) AS average
    FROM second_table;
