with pp as (
    select MEMBER_ID from REST_REVIEW group by MEMBER_ID 
    order by count(distinct REVIEW_ID) desc limit 1
)

select case when r.MEMBER_ID in (select * from pp) 
                then MEMBER_NAME 
        end as MEMBER_NAME, REVIEW_TEXT, date_format(REVIEW_DATE, '%Y-%m-%d') as REVIEW_DATE
from REST_REVIEW r
    join MEMBER_PROFILE m on r.MEMBER_ID = m.MEMBER_ID
having MEMBER_NAME is not null
order by REVIEW_DATE, REVIEW_TEXT

# select MEMBER_ID, count(distinct REVIEW_ID)
# from REST_REVIEW 
# group by MEMBER_ID 
# order by count(distinct REVIEW_ID) desc