-- Script lists all citie with their respective states

-- List all cities with their respective states
SELECT cities.id, cities.name, states.name
FROM cities
INNER JOIN states ON cities.state_id=states.id
ORDER BY cities.id;