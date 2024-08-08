select o.PRODUCT_ID, p.PRODUCT_NAME, SUM(PRICE*AMOUNT) as TOTAL_SALES
from (
    select * from FOOD_ORDER 
    where PRODUCE_DATE between '2022-05-01' and '2022-05-31') o 
    join FOOD_PRODUCT p on p.PRODUCT_ID = o.PRODUCT_ID
group by o.PRODUCT_ID
order by TOTAL_SALES desc , o.PRODUCT_ID asc