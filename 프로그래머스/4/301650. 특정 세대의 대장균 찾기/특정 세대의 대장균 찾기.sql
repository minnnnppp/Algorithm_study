select a.ID
from ECOLI_DATA a 
    left join ECOLI_DATA b on a.PARENT_ID = b.ID
where b.PARENT_ID in (select ID from ECOLI_DATA where PARENT_ID is null)
order by 1;