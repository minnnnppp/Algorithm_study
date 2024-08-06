select year(SALES_DATE) as YEAR, month(SALES_DATE) as MONTH, GENDER
    , count(distinct s.USER_ID) as USERS
from ONLINE_SALE s
    left join USER_INFO u on s.USER_ID = u.USER_ID
where GENDER is not null
group by YEAR, MONTH, GENDER
order by YEAR, MONTH, GENDER