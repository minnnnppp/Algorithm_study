select a.ID, count(distinct b.ID) as CHILD_COUNT
from ECOLI_DATA a
    left join ECOLI_DATA b on a.ID = b.PARENT_ID
group by a.ID
order by a.ID