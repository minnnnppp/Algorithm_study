with recursive times AS(
    select 0 as HOUR # 초기값 설정
    UNION ALL
    select HOUR+1 from times
    where HOUR < 23 # 반복을 멈추는 조건
)

select t.HOUR, count(distinct ANIMAL_ID) as COUNT
from times t
    left join (
        select *, hour(DATETIME) as HOUR 
        from ANIMAL_OUTS) o 
    on t.HOUR = o.HOUR
group by t.HOUR
order by t.HOUR
