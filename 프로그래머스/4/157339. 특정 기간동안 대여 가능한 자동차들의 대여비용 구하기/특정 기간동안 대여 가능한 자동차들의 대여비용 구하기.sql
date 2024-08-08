with types_fees as (
    select CAR_ID, CAR_TYPE, DAILY_FEE
    from CAR_RENTAL_COMPANY_CAR
    where CAR_TYPE in ('세단','SUV' )
), disc as (
    select CAR_TYPE, (100-DISCOUNT_RATE)/100 as TOTAL_RATE
    from CAR_RENTAL_COMPANY_DISCOUNT_PLAN
    where DURATION_TYPE like '30%'
), disable as (
    select distinct CAR_ID
    from CAR_RENTAL_COMPANY_RENTAL_HISTORY
    where END_DATE like '2022-11%' or START_DATE like '2022-11%'
        or (START_DATE < '2022-11-01' and END_DATE > '2022-11-30')
)

select case when CAR_ID not in (select * from disable) then CAR_ID end as CAR_ID
    , f.CAR_TYPE, round((DAILY_FEE*30)*TOTAL_RATE) as FEE
from types_fees f
    join disc d on f.CAR_TYPE = d.CAR_TYPE
having CAR_ID is not null and FEE >= 500000 and FEE < 2000000
order by FEE desc, f.CAR_TYPE asc, CAR_ID desc
