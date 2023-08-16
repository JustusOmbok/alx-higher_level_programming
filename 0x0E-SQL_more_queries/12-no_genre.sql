-- Script that lists shows without a linked genre
-- Uses hbtn_0d_tvshows db
-- Lists all shows

SELECT tv_shows.title, NULL AS genre_id
FROM tv_shows
WHERE tv_shows.id NOT IN (SELECT DISTINCT show_id FROM tv_show_genres)
ORDER BY tv_shows.title;