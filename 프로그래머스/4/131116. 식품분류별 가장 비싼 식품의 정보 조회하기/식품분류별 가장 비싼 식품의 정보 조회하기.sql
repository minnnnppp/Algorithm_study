select CATEGORY, PRICE as MAX_PRICE, PRODUCT_NAME
from (
    select *, rank() over(partition by CATEGORY order by PRICE desc) as rk
    from FOOD_PRODUCT
    where CATEGORY in ('과자', '국', '김치', '식용유')
) pp
where rk = 1
order by MAX_PRICE desc