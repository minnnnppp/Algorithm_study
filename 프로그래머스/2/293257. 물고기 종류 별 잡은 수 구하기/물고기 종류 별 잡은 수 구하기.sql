select count(*) as FISH_COUNT, FISH_NAME
from FISH_INFO f
    left join FISH_NAME_INFO n on f.FISH_TYPE = n.FISH_TYPE
group by FISH_NAME
order by FISH_COUNT desc