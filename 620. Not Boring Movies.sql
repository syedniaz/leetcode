# Write your MySQL query statement below
select *
from Cinema
WHERE mod(id,2) <> 0 AND description <> 'boring'
order by rating desc