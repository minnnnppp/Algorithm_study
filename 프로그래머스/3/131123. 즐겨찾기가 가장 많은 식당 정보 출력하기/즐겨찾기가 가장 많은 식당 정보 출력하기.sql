select FOOD_TYPE, REST_ID, REST_NAME, FAVORITES
from (
    select *, rank() over(partition by FOOD_TYPE order by FAVORITES desc) as RK
    from REST_INFO
) as pp
where RK = 1
order by FOOD_TYPE desc