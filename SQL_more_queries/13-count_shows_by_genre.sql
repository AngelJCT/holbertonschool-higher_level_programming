-- lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each
SELECT genres.name, COUNT(tv_show_genres.genre_id) AS number_of_shows
FROM genres
LEFT JOIN tv_show_genres
ON genres.id = tv_show_genres.genre_id
GROUP BY genres.name
ORDER BY num_shows DESC, genres.name ASC;