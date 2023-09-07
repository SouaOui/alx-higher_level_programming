-- displays the average temperature (Fahrenheit) by city ordered by temperature (descending)
-- ONLY top 3 LIMIT top three 
SELECT city, AVG(value) AS avg_temp FROM temperatures GROUP BY city ORDER BY avg_temp DESC LIMIT 3;
