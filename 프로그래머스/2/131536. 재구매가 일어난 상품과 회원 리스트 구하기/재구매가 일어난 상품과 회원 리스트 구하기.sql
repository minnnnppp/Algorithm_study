select USER_ID, PRODUCT_ID
from (
    select USER_ID, PRODUCT_ID, count(distinct ONLINE_SALE_ID) as CNT
    from ONLINE_SALE
    group by USER_ID, PRODUCT_ID
) pp
where CNT > 1
order by USER_ID asc, PRODUCT_ID desc