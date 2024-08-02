select e.DEPT_ID, DEPT_NAME_EN, round(avg(SAL)) as AVG_SAL
from HR_EMPLOYEES e
    left join HR_DEPARTMENT d on e.DEPT_ID = d.DEPT_ID
group by e.DEPT_ID
order by AVG_SAL desc