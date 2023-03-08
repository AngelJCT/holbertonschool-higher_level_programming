-- create a second table and add multiple rows
CREATE TABLE IF NOT EXISTS second_table (
    id INT NOT NULL PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(256) NOT NULL,
    score INT
);