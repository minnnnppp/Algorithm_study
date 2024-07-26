select t.ITEM_ID, ITEM_NAME
from ITEM_TREE t 
    left join ITEM_INFO i on t.ITEM_ID = i.ITEM_ID
where PARENT_ITEM_ID is null
order by t.ITEM_ID