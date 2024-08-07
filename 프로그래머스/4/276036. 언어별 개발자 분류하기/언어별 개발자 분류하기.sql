# with ad as (
#     select ID
#     from DEVELOPERS
#     where SKILL_CODE & (select CODE from SKILLCODES where NAME = 'Python')
#         and SKILL_CODE & (select sum(CODE) from SKILLCODES where CATEGORY = 'Front End')
# ), bd as (
#     select ID
#     from DEVELOPERS
#     where SKILL_CODE & (select CODE from SKILLCODES where NAME = 'C#')
# )
# , cd as (
#     select ID
#     from DEVELOPERS
#     where (ID not in (select ID from ad)) and (ID not in (select ID from bd))
#         and (SKILL_CODE & (select sum(CODE) from SKILLCODES where CATEGORY = 'Front End'))
# )

select case when 
            SKILL_CODE & (select CODE from SKILLCODES where NAME = 'Python')
            and SKILL_CODE & (
                select sum(CODE) from SKILLCODES 
                where CATEGORY = 'Front End'
            ) then 'A'
            when SKILL_CODE & (select CODE from SKILLCODES where NAME = 'C#') then 'B'
            when SKILL_CODE & (
                select sum(CODE) from SKILLCODES 
                where CATEGORY = 'Front End'
            ) then 'C'
        end as GRADE, ID, EMAIL
from DEVELOPERS
having GRADE is not null
order by GRADE, ID