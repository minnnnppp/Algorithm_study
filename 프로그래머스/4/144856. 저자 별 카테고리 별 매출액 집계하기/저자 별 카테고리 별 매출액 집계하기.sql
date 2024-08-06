select b.AUTHOR_ID, AUTHOR_NAME, CATEGORY
    , sum(PRICE*SALES) as TOTAL_SALES
from BOOK_SALES s
    join BOOK b on s.BOOK_ID = b.BOOK_ID    
    join AUTHOR a on b.AUTHOR_ID = a.AUTHOR_ID
where SALES_DATE between '2022-01-01' and '2022-01-31'
group by b.AUTHOR_ID, CATEGORY
order by b.AUTHOR_ID asc, CATEGORY desc