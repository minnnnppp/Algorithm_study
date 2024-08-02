with pp as (
    select CAR_ID
    from CAR_RENTAL_COMPANY_RENTAL_HISTORY
    where START_DATE between '2022-08-01' and '2022-10-31'
    group by CAR_ID
    having count(distinct HISTORY_ID) >= 5
)

select month(START_DATE) as MONTH, CAR_ID
    , count(distinct HISTORY_ID) as RECORDS
from (
    select *
    from CAR_RENTAL_COMPANY_RENTAL_HISTORY
    where CAR_ID in (select * from pp)
) as pps
where START_DATE between '2022-08-01' and '2022-10-31'
group by MONTH, CAR_ID
having RECORDS > 0
order by MONTH asc, CAR_ID desc