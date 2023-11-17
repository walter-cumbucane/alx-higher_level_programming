-- Calculates the average temperature in each city

SELECT city, AVG(*) AS avg_temp FROM temperatures GROUP BY city ORDER BY avg_temp DESC;