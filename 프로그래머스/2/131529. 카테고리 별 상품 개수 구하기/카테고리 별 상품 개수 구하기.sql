select substring(PRODUCT_CODE, 1, 2) as CATEGORY
    , count(distinct PRODUCT_ID) as PRODUCTS
from PRODUCT
group by CATEGORY
order by CATEGORY