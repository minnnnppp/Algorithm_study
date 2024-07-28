select count(distinct case when NAME is not null then NAME end) as count
from ANIMAL_INS