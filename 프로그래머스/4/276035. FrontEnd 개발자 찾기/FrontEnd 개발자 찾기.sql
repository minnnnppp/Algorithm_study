select distinct ID, EMAIL, FIRST_NAME, LAST_NAME
from DEVELOPERS d
    join (select * from SKILLCODES where CATEGORY = 'Front End') s 
    on d.SKILL_CODE&s.CODE = s.CODE
order by ID