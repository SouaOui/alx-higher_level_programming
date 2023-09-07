-- Convert the DATABASE to utf-8 and also the table and field name
USE hbtn_0c_0;
ALTER DATABASE hbtn_0c_0 CHARACTER SET utf8 COLLATE utf8_general_ci;
ALTER TABLE first_table CONVERT TO CHARACTER SET utf8 COLLATE utf8_general_ci;
ALTER TABLE first_table MODIFY name VARCHAR(255) CHARACTER SET utf8 COLLATE utf8_general_ci;

