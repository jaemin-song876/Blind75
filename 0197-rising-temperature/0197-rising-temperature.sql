# Write your MySQL query statement below

select today.id
from Weather as today
join Weather as yesterday on today.recordDate = yesterday.recordDate+ interval 1 day
where today.temperature > yesterday.temperature
