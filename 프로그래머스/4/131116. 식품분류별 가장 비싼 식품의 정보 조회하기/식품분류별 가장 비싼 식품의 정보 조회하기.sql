select CATEGORY, PRICE as MAX_PRICE, PRODUCT_NAME
from FOOD_PRODUCT
where (CATEGORY, PRICE) in (select distinct CATEGORY
                           , max(PRICE) over(partition by CATEGORY) as MAX_PRICE
                           from FOOD_PRODUCT)
    and CATEGORY in ('과자', '국', '김치', '식용유')
order by MAX_PRICE desc;