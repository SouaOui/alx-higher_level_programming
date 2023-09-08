-- create a user and grant them all permisions on your sql server
CREATE DATABASE hbtn_0d_2 IF NOT EXISTS;
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT ON hbtn_0d_2 TO 'user_0d_2'@'localhost';
