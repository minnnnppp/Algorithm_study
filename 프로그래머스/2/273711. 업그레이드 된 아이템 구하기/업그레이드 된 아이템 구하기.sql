with rr as (
    select ITEM_ID
    from ITEM_INFO
    where RARITY = 'RARE'
)

select i.ITEM_ID, ITEM_NAME, RARITY
from ITEM_INFO i 
    left join ITEM_TREE t on i.ITEM_ID = t.ITEM_ID
where t.PARENT_ITEM_ID in (select * from rr)
order by i.ITEM_ID desc