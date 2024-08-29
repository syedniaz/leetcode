# Write your MySQL query statement below
select sell_date, count(DISTINCT product) AS num_sold, 
    GROUP_CONCAT(DISTINCT product
                ORDER BY product ASC) AS products
from Activities
group by sell_date