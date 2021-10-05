# Write your MySQL query statement below
SELECT e1.name as Employee FROM Employee e1
WHERE EXISTS (SELECT 1 FROM Employee e2 WHERE e1.salary > e2.salary AND e1.ManagerId = e2.id)