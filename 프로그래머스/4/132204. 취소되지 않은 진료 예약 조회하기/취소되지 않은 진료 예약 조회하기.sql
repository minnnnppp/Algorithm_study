select APNT_NO, PT_NAME, a.PT_NO, a.MCDP_CD, DR_NAME, APNT_YMD
from APPOINTMENT a 
    join PATIENT p on a.PT_NO = p.PT_NO
    join DOCTOR d on a.MDDR_ID = d.DR_ID
where date_format(APNT_YMD, '%Y-%m-%d') = '2022-04-13' 
    and APNT_CNCL_YN = 'N' and a.MCDP_CD = 'CS'
order by APNT_YMD;