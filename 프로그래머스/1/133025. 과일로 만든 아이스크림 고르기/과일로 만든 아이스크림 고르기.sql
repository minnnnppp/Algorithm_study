select f.FLAVOR
from FIRST_HALF as f
    left join ICECREAM_INFO as i on f.FLAVOR = i.FLAVOR
where INGREDIENT_TYPE = 'fruit_based' and TOTAL_ORDER > 3000
order by TOTAL_ORDER desc