select hour(DATETIME) as HOUR, count(distinct ANIMAL_ID) as COUNT
from ANIMAL_OUTS
where hour(DATETIME) between 9 and 19
group by HOUR
order by HOUR asc