select distinct CAR_ID, 
    case when CAR_ID in (
            select CAR_ID
            from CAR_RENTAL_COMPANY_RENTAL_HISTORY
            where date_format(START_DATE, '%Y-%m-%d') <= '2022-10-16' 
                and date_format(END_DATE, '%Y-%m-%d') >= '2022-10-16' ) 
        then '대여중'
        else '대여 가능' end as AVAILABILITY
from CAR_RENTAL_COMPANY_RENTAL_HISTORY
order by CAR_ID desc;