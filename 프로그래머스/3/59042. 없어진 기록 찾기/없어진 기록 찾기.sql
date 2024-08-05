select o.ANIMAL_ID, o.NAME
from ANIMAL_OUTS o
    left join ANIMAL_INS i on o.ANIMAL_ID = i.ANIMAL_ID
where i.DATETIME is null
order by o.ANIMAL_ID