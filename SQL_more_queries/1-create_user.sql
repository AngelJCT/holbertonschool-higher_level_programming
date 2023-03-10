-- create MySQL server for user_0d_1
CREATE USER 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL ON *.* TO 'user_0d_1'@'localhost' WITH GRANT OPTION;