-- Script that lists all genres and number of shows
-- Uses hbtn_0d_tvshows db
-- Lists genres and and number of linked shows

SELECT tv_genres.name AS genre, COUNT(*) AS number_of_shows
FROM tv_genres
INNER JOIN tv_show_genres
ON tv_genres.id=tv_show_genres.genre_id
GROUP BY tv_show_genres.genre_id
ORDER BY number_of_shows DESC;