# Write your MySQL query statement below
select p.email
from person as p
group by email
having count(*)>1;
