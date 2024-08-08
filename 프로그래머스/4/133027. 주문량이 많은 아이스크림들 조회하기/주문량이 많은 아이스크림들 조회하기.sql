with ju as (
    select FLAVOR, sum(TOTAL_ORDER) as TOTAL_ORDER
    from JULY
    group by FLAVOR
), fh as (
    select FLAVOR, sum(TOTAL_ORDER) as TOTAL_ORDER
    from FIRST_HALF
    group by FLAVOR
), ts as (
    select j.FLAVOR, (j.TOTAL_ORDER+h.TOTAL_ORDER) as TOTAL_ORDER
    from ju j
        join fh h on j.FLAVOR = h.FLAVOR
)

select j.FLAVOR
from ju j
    join fh h on j.FLAVOR = h.FLAVOR
order by (j.TOTAL_ORDER+h.TOTAL_ORDER) desc
limit 3