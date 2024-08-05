with pr as (
    select ID
    from ECOLI_DATA
    where PARENT_ID is null
), frs as (
    select ID
    from ECOLI_DATA
    where PARENT_ID in (select * from pr)
)

select ID
from ECOLI_DATA
where PARENT_ID in (select * from frs)
order by ID