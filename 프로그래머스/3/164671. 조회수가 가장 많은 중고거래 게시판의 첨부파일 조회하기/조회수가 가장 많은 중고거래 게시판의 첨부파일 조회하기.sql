select concat('/home/grep/src/', BOARD_ID, '/', FILE_ID, FILE_NAME, FILE_EXT) as FILE_PATH
from USED_GOODS_BOARD natural join USED_GOODS_FILE
where VIEWS = (select max(VIEWS) from USED_GOODS_BOARD)
order by FILE_ID desc