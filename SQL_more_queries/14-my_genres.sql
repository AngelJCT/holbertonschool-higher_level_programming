-- script that uses the hbtn_0d_tvshows database to list all genres of the show Dexter
SELECT tv_show.title, tv.genres.name
FROM tv_show
INNER JOIN tv_show_genres
ON tv_show.id = tv_show_genres.show_id
INNER JOIN tv_genres
ON tv_show_genres.genre_id = tv_genres.id
WHERE tv_show.title = 'Dexter'
ORDER BY tv_genres.name ASC;