# Write your MySQL query statement below
SELECT DISTINCT l1.num AS ConsecutiveNums
from Logs l1
INNER JOIN Logs l2 on l2.id = l1.id + 1 and l2.num = l1.num
INNER JOIN Logs l3 on l3.id = l2.id + 1 and l3.num = l2.num