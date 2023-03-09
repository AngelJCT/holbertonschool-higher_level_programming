-- list all records of the table second_table
SELECT score, name FROM second_table WHERE name IS NOT NULL OR IS NULL ORDER BY score DESC, name DESC;