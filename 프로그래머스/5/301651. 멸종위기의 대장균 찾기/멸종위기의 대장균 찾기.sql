with recursive generations as (
    select ID, 1 as GENERATION
    from ECOLI_DATA
    where PARENT_ID is null
    union all
    select a.ID, GENERATION+1 
    from ECOLI_DATA a
        join generations g on g.ID = a.PARENT_ID
)

select count(distinct a.ID) as COUNT, GENERATION
from ECOLI_DATA a
    join generations c on a.ID = c.ID
    left join ECOLI_DATA b on b.PARENT_ID = a.ID
where b.ID is null
group by GENERATION
order by GENERATION;