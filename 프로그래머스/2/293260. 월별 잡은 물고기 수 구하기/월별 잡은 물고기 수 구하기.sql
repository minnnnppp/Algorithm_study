select count(distinct ID) as FISH_COUNT
    , month(TIME) as MONTH
from FISH_INFO
group by MONTH
having FISH_COUNT >0
order by MONTH