with maxx as (
    select CATEGORY, max(PRICE) as MAX_PRICE
    from FOOD_PRODUCT
    where CATEGORY in ('과자', '국', '김치', '식용유')
    group by CATEGORY
)

select p.CATEGORY, MAX_PRICE
    , case when PRICE = MAX_PRICE then PRODUCT_NAME end as PRODUCT_NAME
from FOOD_PRODUCT p
    join maxx m on p.CATEGORY = m.CATEGORY
having PRODUCT_NAME is not null
order by MAX_PRICE desc