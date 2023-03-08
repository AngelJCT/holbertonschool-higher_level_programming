-- create a table in the current database
-- first column: id with datatype and set as primary key that will auto-increment with each new record added
-- second column: name withe length of 256 chars with NOT NULL constraint to ensure that must have a value
CREATE TABLE IF NOT EXISTS first_table (
    id INT,
    name VARCHAR(256),
);