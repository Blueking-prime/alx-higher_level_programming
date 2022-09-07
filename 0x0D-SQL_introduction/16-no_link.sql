-- a script that lists all records of the table second_table of the database

-- Lists the records
SELECT `score`, `name`
    FROM second_table
    ORDER BY `score` DESC, `name` DESC;
