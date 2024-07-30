select case 
        when PRICE >= 10000 then truncate(PRICE, -4) 
        else 0
    end as PRICE_GROUP
    , count(distinct PRODUCT_ID) as PRODUCTS
from PRODUCT 
group by PRICE_GROUP
order by PRICE_GROUP