select FLAVOR
from FIRST_HALF
group by FLAVOR
order by sum(TOTAL_ORDER) desc, SHIPMENT_ID asc