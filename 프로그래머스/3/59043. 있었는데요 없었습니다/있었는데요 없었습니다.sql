select i.ANIMAL_ID, i.NAME
from ANIMAL_INS i
    join ANIMAL_OUTS o on i.ANIMAL_ID = o.ANIMAL_ID
where o.DATETIME < i.DATETIME
order by i.DATETIME