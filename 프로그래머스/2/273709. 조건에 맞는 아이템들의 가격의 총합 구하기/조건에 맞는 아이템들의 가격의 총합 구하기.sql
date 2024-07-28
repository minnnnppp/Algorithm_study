select sum(
        case when RARITY = 'LEGEND' then PRICE end
    ) as TOTAL_PRICE
from ITEM_INFO