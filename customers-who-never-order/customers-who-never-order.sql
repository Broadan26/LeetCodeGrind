# Write your MySQL query statement below
SELECT c1.Name AS Customers FROM Customers c1
WHERE NOT EXISTS (SELECT 1 FROM Orders o1 WHERE o1.CustomerId = c1.Id)