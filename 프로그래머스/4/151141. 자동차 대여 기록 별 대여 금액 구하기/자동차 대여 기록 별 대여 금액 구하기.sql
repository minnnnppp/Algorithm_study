with rent_history_type as (
    select HISTORY_ID, CAR_TYPE, datediff(END_DATE, START_DATE)+1 as duration
        , DAILY_FEE
        , case 
            when datediff(END_DATE, START_DATE)+1 >= 90 then '90일 이상'
            when datediff(END_DATE, START_DATE)+1 >= 30 then '30일 이상'
            when datediff(END_DATE, START_DATE)+1 >= 7 then '7일 이상'
        else null end as DURATION_TYPE
    from CAR_RENTAL_COMPANY_RENTAL_HISTORY h
        left join CAR_RENTAL_COMPANY_CAR c on h.CAR_ID = c.CAR_ID
    where CAR_TYPE = '트럭'
), only_truck as (
    select *
    from CAR_RENTAL_COMPANY_DISCOUNT_PLAN
    where CAR_TYPE = '트럭'
)

select HISTORY_ID
    , case 
        when discount_rate is not null 
            then round((DAILY_FEE*duration)*((100-discount_rate)/100))
        else round(DAILY_FEE*duration)
    end as FEE
from rent_history_type t
    left join only_truck d on t.DURATION_TYPE = d.DURATION_TYPE
order by FEE desc, HISTORY_ID desc