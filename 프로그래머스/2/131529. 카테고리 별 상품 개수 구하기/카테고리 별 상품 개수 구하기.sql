select CATEGORY, count(distinct PRODUCT_ID) as PRODUCTS
from (
    select *, substring(PRODUCT_CODE, 1, 2) as CATEGORY
    from PRODUCT
) pp
group by CATEGORY
order by 1;