select case when rk = 1 then ID end as ID, FISH_NAME, LENGTH
from (    
    select *, rank() over(partition by FISH_TYPE order by LENGTH desc) as rk
    from FISH_INFO 
) i
    join FISH_NAME_INFO n on i.FISH_TYPE = n.FISH_TYPE
having ID is not null
order by 1;