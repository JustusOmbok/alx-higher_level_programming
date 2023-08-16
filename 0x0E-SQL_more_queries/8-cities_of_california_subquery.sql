-- Script lists cities of Califonia state

-- Using the database
USE hbtn_0d_usa;

-- List cities in California
SELECT cities.id, cities.name
FROM cities
WHERE cities.state_id = (
    SELECT id
    FROM states
    WHERE name = 'California'
)
ORDER BY cities.id;