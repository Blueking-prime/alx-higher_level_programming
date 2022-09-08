-- a script that creates the MySQL server user user_0d_1
-- Create user
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost'
           IDENTIFIED BY 'user_0d_1_pwd';

-- Save changes
FLUSH PRIVILEGES;

-- Grant permissions
GRANT ALL PRIVILEGES ON *.*
   TO 'user_0d_1'@'localhost'
 WITH GRANT OPTION;

-- Save changes
FLUSH PRIVILEGES;
