# Write your MySQL query statement below
SELECT Email as Email
FROM Person
GROUP BY Email
HAVING COUNT(*) > 1