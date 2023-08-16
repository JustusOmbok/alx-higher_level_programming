-- Script lists all citie with their respective states

-- Using the database
USE hbtn_0d_usa;

-- List all cities with their respective states
SELECT cities.id, cities.name, states.name
FROM cities
INNER JOIN states ON cities.state_id = states.id
ORDER BY cities.id;