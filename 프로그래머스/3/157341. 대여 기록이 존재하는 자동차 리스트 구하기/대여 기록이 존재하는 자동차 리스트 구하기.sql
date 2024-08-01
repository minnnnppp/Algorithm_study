select distinct CAR_ID
from CAR_RENTAL_COMPANY_RENTAL_HISTORY natural join CAR_RENTAL_COMPANY_CAR
where CAR_TYPE = '세단' and START_DATE >= '2022-10-01'
order by CAR_ID desc