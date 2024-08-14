with max_by_year as (
    select YEAR(DIFFERENTIATION_DATE) as YEAR, max(SIZE_OF_COLONY) MAX_SIZE
    from ECOLI_DATA
    group by YEAR
)

select e.YEAR, (MAX_SIZE-SIZE_OF_COLONY) as YEAR_DEV, ID
from (select *, YEAR(DIFFERENTIATION_DATE) as YEAR from ECOLI_DATA) e
    left join max_by_year m on e.YEAR = m.YEAR
order by 1, 2;