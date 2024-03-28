# WITH CHILDS AS (
#     SELECT T1.ITEM_ID, T1.PARENT_ITEM_ID, T2.ITEM_ID AS CHILD_ID
#     FROM ITEM_TREE T1
#         JOIN ITEM_TREE T2 ON T1.ITEM_ID = T2.PARENT_ITEM_ID
#     HAVING CHILD_ID IS NULL
# )

SELECT ITEM_ID, ITEM_NAME, RARITY
FROM ITEM_INFO
WHERE ITEM_ID NOT IN (
    SELECT PARENT_ITEM_ID 
    FROM ITEM_TREE 
    WHERE PARENT_ITEM_ID IS NOT NULL)
ORDER BY ITEM_ID DESC
