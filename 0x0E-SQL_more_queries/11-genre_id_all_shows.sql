-- Script that lists all shows with genre ids or null
-- Uses hbtn_0d_tvshowa db
-- Lists all shows

SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_genres
ON tv_shows.id=tv_show_genres.show_id
ORDER BY tv_shows.title, tv_show_genres.genre_id;