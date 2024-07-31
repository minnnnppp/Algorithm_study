with pp as (
    select ID, SIZE_OF_COLONY, percent_rank() over(order by SIZE_OF_COLONY desc) as RK
    from ECOLI_DATA
)

select ID, 
    case when RK*100 <= 25 then 'CRITICAL'
        when RK*100 <= 50 then 'HIGH'
        when RK*100 <= 75 then 'MEDIUM'
        else 'LOW'    
    end as COLONY_NAME
from pp
order by ID