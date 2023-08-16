-- Script to list shows linke with genres
-- Uses the hbtn_0d_tvshows database
-- Lists shows with linked genres

SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
INNER JOIN tv_show_genres 
ON tv_shows.id=tv_show_genres.show_id
ORDER BY tv_shows.title, tv_show_genres.genre_id;