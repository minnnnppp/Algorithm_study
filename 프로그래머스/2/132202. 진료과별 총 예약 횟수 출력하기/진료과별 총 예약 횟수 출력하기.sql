select MCDP_CD as '진료과코드', count(*) as '5월예약건수'
from APPOINTMENT
where date_format(APNT_YMD, '%Y-%m-%d') between '2022-05-01' and '2022-05-31'
group by MCDP_CD
order by COUNT(*),MCDP_CD