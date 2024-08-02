select CATEGORY, sum(SALES) as TOTAL_SALES
from BOOK_SALES s
    left join BOOK b on s.BOOK_ID = b.BOOK_ID
where SALES_DATE between '2022-01-01' and '2022-01-31'
group by CATEGORY
order by CATEGORY