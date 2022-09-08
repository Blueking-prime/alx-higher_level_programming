-- a script that lists all the cities of California that can be found in the database hbtn_0d_usa
-- List cities in california
  SELECT `id`, `name`
    FROM cities
   WHERE state_id =
        ( -- Finds california's state id
        SELECT `id`
          FROM states
         WHERE name = 'California')
ORDER BY id ASC;
