-- list the number of records with the same score in second_table
SELECT score, COUNT(score) AS number FROM second_table ORDER BY score DESC, name DESC GROUP BY score;