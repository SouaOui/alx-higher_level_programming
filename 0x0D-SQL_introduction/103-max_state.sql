-- displays the average temperature (Fahrenheit) by city ordered by temperature (descending)
-- ONLY top 3 LIMIT top three 
SELECT state, MAX(value) AS max_temp FROM temperatures GROUP BY state ORDER BY state;
