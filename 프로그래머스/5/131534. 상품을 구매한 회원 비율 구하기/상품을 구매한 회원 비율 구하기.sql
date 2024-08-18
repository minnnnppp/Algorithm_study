with targets as (
    select *
    from USER_INFO
    where YEAR(JOINED) = 2021
)

select YEAR(SALES_DATE) as YEAR
    , MONTH(SALES_DATE) as MONTH
    , count(distinct case 
                when USER_ID in (select USER_ID from targets) then USER_ID end
    ) as PURCHASED_USERS
    , round((count(
        distinct case when USER_ID in (select USER_ID from targets) then USER_ID end)/
             (select count(distinct USER_ID) from targets)), 1) as PUCHASED_RATIO
from ONLINE_SALE
group by YEAR, MONTH
order by 1, 2;