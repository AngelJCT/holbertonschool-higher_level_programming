-- lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each
SELECT tv_genres.name AS genre, COUNT(*) AS number_of_shows
FROM tv_show_genres
GROUP BY genre
HAVING COUNT(*) > 0
ORDER BY number_of_shows DESC;