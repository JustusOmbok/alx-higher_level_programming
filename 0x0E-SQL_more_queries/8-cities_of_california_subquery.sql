-- Script lists cities of Califonia state
-- List cities in California
-- Results sorted ascending by cities
--Not allowed to use join


SELECT id, name 
FROM cities 
WHERE state_id = (SELECT id FROM states WHERE name = "California") ORDER BY id;