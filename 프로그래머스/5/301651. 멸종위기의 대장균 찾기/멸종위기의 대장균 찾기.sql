with recursive BY_GENERATION as (
    select ID, 1 as GENERATION
    from ECOLI_DATA
    where PARENT_ID is null
    UNION ALL
    SELECT a.ID, b.GENERATION+1 as GENERATION
    from ECOLI_DATA a
        join BY_GENERATION b on a.PARENT_ID = b.ID
)

select count(distinct a.ID) as COUNT, GENERATION
from ECOLI_DATA a
    join BY_GENERATION b on a.ID = b.ID
    left join ECOLI_DATA c on a.ID = c.PARENT_ID
where c.ID is null
group by GENERATION
order by GENERATION