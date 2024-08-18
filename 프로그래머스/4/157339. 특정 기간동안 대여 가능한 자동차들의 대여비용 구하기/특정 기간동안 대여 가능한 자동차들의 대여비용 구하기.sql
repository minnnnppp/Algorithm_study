with car_type as (
    select * 
    from CAR_RENTAL_COMPANY_CAR 
    where CAR_TYPE in ('세단' , 'SUV' )
), inavaliables as (
    select *
    from CAR_RENTAL_COMPANY_RENTAL_HISTORY
    where (date_format(START_DATE, '%Y-%m-%d') <= '2022-11-30' 
           and date_format(END_DATE, '%Y-%m-%d') >= '2022-11-01') 
)
    
select distinct h.CAR_ID, c.CAR_TYPE
    , case when (daily_fee*30)*(1-discount_rate/100) >= 500000 
            and (daily_fee*30)*(1-discount_rate/100) < 2000000 
        then round((daily_fee*30)*(1-discount_rate/100)) 
    end as FEE
from CAR_RENTAL_COMPANY_RENTAL_HISTORY h
    left join car_type c on c.CAR_ID = h.CAR_ID
    left join (select * from CAR_RENTAL_COMPANY_DISCOUNT_PLAN 
               where DURATION_TYPE like '30%') p on c.CAR_TYPE = p.CAR_TYPE
where h.CAR_ID not in (select CAR_ID from inavaliables)
having FEE is not null
order by 1 asc, 2 desc;