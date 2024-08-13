with pp as (
    select *, rank() over(order by SIZE_OF_COLONY desc) as RK
    from ECOLI_DATA
)

select ID, case when (RK/(select max(RK) from pp))*100 <= 25 then 'CRITICAL'
                when (RK/(select max(RK) from pp))*100 <= 50 then 'HIGH'
                when (RK/(select max(RK) from pp))*100 <= 75 then 'MEDIUM'      
                else 'LOW'        
    end as COLONY_NAME
from pp
order by ID