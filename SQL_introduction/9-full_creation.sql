-- create a second table and add multiple rows
CREATE TABLE IF NOT EXISTS second_table (
    id INT NOT NULL PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(256) NOT NULL,
    score INT
);
INSERT INTO second_table (name, score) VALUES
    (1, 'John', 10),
    (2, 'Alex', 3),
    (3, 'Bob', 14),
    (4, 'George', 8);