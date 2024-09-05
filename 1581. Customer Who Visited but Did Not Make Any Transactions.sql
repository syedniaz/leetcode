# Write your MySQL query statement below
select v.customer_id, count(v.customer_id) as count_no_trans
from Visits v
LEFT JOIN Transactions t ON v.visit_id = t.visit_id
where t.visit_id is null
Group by v.customer_id