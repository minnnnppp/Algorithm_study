select ANIMAL_ID, NAME
from ANIMAL_INS
where ANIMAL_TYPE = 'Dog' and NAME like '%el%' 
# or NAME like '%El%' or NAME like '%EL%' or NAME like '%eL%'
order by NAME