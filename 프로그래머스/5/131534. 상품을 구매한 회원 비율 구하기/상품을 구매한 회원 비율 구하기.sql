# 21년 가입자
with us_21 as (
    select *
    from USER_INFO
    where year(JOINED) = 2021
), sales as (
    select u.USER_ID as JOIN_USER_ID, JOINED
        , o.USER_ID as SALE_USER_ID, SALES_DATE
    from us_21 u
        left join ONLINE_SALE o on o.USER_ID=u.USER_ID
)

# select * from sales
select year(SALES_DATE) as YEAR, month(SALES_DATE) as MONTH
    , count(distinct SALE_USER_ID) as PURCHASED_USERS
    , round(count(distinct SALE_USER_ID) / (select count(distinct JOIN_USER_ID) from sales), 1) as PUCHASED_RATIO
from sales
group by MONTH
having YEAR is not null
order by 1, 2