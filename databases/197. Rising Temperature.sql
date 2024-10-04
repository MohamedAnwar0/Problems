# Write your MySQL query statement below
SELECT w.id FROM weather w
join weather s
 WHERE w.temperature > s.temperature
 AND DATEDIFF(w.Recorddate, s.Recorddate) = 1;
