-- Script that lists all genres not linked to sho Dexter
-- Uses hbtn_0d_tvshows db
-- Lists all genres not linked to Dexter

SELECT tv_genres.name
FROM tv_genres
WHERE tv_genres.id NOT IN (SELECT genre_id FROM tv_show_genres WHERE show_id = (SELECT id FROM tv_shows WHERE title = 'Dexter'))
ORDER BY tv_genres.name;