-- Script that lists all genres and number of shows
-- Uses hbtn_0d_tvshows db
-- Lists genres and and number of linked shows
SELECT genres.name AS genre, COUNT(tv_show_genres.show_id) AS number_of_shows
FROM generes
LEFT JOIN tv_show_genres
ON genres.id=tv_show_genres.genre_id
GROUP BY genres.name
HAVING COUNT(tv_show_genres.show_id) > 0
ORDER BY number_of_shows DESC;