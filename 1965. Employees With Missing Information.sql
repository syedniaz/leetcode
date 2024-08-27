# Write your MySQL query statement below
select e.employee_id
from Employees e
left join Salaries s on e.employee_id = s.employee_id
WHERE S.salary IS NULL
union 
select s.employee_id
from Employees e
right join Salaries s on e.employee_id = s.employee_id
WHERE e.Name IS NULL
ORDER BY employee_id