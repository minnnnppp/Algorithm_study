with pp as (    
    select EMP_NO, sum(SCORE) as SCORE
    from HR_GRADE
    group by EMP_NO
)

select SCORE, p.EMP_NO, EMP_NAME, POSITION, EMAIL
from pp p
    left join HR_EMPLOYEES e on p.EMP_NO = e.EMP_NO
where SCORE = (select max(SCORE) from pp)