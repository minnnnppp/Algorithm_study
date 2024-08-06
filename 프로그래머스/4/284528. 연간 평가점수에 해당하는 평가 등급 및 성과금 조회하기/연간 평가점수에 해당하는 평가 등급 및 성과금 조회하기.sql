select g.EMP_NO, EMP_NAME
    , case 
        when AVG_SCORE >= 96 then 'S'
        when AVG_SCORE >= 90 then 'A'
        when AVG_SCORE >= 80 then 'B'
        else 'C'
    end as GRADE
    , case 
        when AVG_SCORE >= 96 then round((SAL*0.2))
        when AVG_SCORE >= 90 then round((SAL*0.15))
        when AVG_SCORE >= 80 then round((SAL*0.1))
        else 0
    end as BONUS
from (
    select EMP_NO, avg(SCORE) as AVG_SCORE
    from HR_GRADE
    group by EMP_NO
) g
    join HR_EMPLOYEES e on g.EMP_NO = e.EMP_NO
order by g.EMP_NO