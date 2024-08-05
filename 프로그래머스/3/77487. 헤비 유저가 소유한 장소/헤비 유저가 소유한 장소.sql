with pp as (
    select HOST_ID
    from PLACES
    group by HOST_ID
    having count(distinct ID) > 1
) 

select *
from PLACES
where HOST_ID in (select * from pp)
order by ID