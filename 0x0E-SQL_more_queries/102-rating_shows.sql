-- Script that lists all their ratings sum
-- Uses hbtn_0d_tvshows_rate db
-- Lists shows by their ratings

SELECT tv_shows.title, SUM(tv_show_ratings.rate) AS rating
FROM tv_shows
INNER JOIN tv_show_ratings 
ON tv_shows.id = tv_show_ratings.show_id
GROUP BY tv_shows.id
ORDER BY rating DESC;