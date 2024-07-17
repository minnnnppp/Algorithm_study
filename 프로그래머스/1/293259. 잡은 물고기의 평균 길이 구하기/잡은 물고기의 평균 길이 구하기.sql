select round(AVG(LENGTH), 2) as AVERAGE_LENGTH
from (
    select ID, FISH_TYPE, TIME
        , case when LENGTH is null then 10 else LENGTH end as LENGTH
    from FISH_INFO
) as prep