with more_5 as (
    select CAR_ID
    from CAR_RENTAL_COMPANY_RENTAL_HISTORY
    where date_format(START_DATE, '%Y-%m-%d') between '2022-08-01' and '2022-10-31'
    group by CAR_ID
    having count(distinct HISTORY_ID) >= 5
)

select month(START_DATE) as MONTH, CAR_ID, count(distinct HISTORY_ID) as RECORDS
from CAR_RENTAL_COMPANY_RENTAL_HISTORY
where date_format(START_DATE, '%Y-%m-%d') between '2022-08-01' and '2022-10-31'
    and CAR_ID in (select * from more_5)
group by CAR_ID, MONTH
order by 1 asc, 2 desc;