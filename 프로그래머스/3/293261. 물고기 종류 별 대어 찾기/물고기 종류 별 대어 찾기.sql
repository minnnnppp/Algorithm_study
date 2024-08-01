select ID, FISH_NAME, LENGTH
from (
    select ID, i.FISH_TYPE, FISH_NAME, LENGTH
        , rank() over(partition by i.FISH_TYPE order by LENGTH desc) as rk
    from FISH_INFO i
        left join FISH_NAME_INFO n on i.FISH_TYPE = n.FISH_TYPE
    where LENGTH is not null
) as pp 
where rk = 1
order by ID