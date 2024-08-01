select distinct i.USER_ID, NICKNAME
    , concat(CITY, ' ', STREET_ADDRESS1, ' ', STREET_ADDRESS2) as '전체주소'
    , concat(substring(TLNO, 1, 3), '-', substring(TLNO, 4, 4), '-', substring(TLNO, 8, 4)) as '전화번호'
from USED_GOODS_BOARD b
    join USED_GOODS_USER i on b.WRITER_ID = i.USER_ID
group by i.USER_ID
having count(distinct BOARD_ID) >=3 
order by i.USER_ID desc