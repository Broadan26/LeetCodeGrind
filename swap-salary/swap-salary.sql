# Write your MySQL query statement below
UPDATE Salary
SET sex = 
    CASE sex
        when 'f' then 'm'
        when 'm' then 'f'
        else sex
    END