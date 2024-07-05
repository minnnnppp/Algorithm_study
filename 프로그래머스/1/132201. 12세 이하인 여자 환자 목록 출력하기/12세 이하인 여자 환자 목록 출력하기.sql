select PT_NAME, PT_NO, GEND_CD, AGE, case when TLNO is null then 'NONE' else TLNO end as TLNO
from PATIENT
where AGE < 13 and GEND_CD = 'W'
order by AGE DESC, PT_NAME ASC