select ID, FISH_NAME, LENGTH
from FISH_INFO i
    join FISH_NAME_INFO n on i.FISH_TYPE = n.FISH_TYPE
where (i.FISH_TYPE, LENGTH) in (
    select FISH_TYPE, max(LENGTH) over(partition by FISH_TYPE) from FISH_INFO)
order by 1;