with recursive hours as (
    select 0 as HOUR
    union all
    select HOUR+1 as HOUR
    from hours
    where HOUR < 23
)

select h.HOUR, count(distinct ANIMAL_ID) as COUNT
from hours h
    left join (select ANIMAL_ID, hour(DATETIME) as HOUR 
               from ANIMAL_OUTS) o 
    on h.HOUR = o.HOUR
group by h.HOUR
order by 1;