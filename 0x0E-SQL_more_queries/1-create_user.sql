-- Script creates user
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost'; IDENTIFIED BY 'user_0d_1_pwd';

-- grants all privilleges to user
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';

-- Flushes privileges to apply changes
FLUSH PRIVILEGES;
