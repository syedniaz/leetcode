# Write your MySQL query statement below
with 
    cte1 as (select machine_id, process_id, sum(timestamp) as start_time from Activity where activity_type = 'start' group by machine_id, process_id),
    cte2 as (select machine_id, process_id, sum(timestamp) as end_time from Activity where activity_type = 'end' group by machine_id, process_id)
select cte1.machine_id, cast((avg(end_time-start_time)) as decimal(10,3)) as processing_time
from cte1
join cte2 on cte1.machine_id = cte2.machine_id
group by machine_id