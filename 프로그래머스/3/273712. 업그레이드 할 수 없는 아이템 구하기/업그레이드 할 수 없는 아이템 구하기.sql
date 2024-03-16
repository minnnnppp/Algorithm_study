-- 코드를 작성해주세요
SELECT I.ITEM_ID,ITEM_NAME,RARITY
FROM ITEM_INFO I 
    LEFT JOIN ITEM_TREE T ON T.PARENT_ITEM_ID = I.ITEM_ID
WHERE T.ITEM_ID IS NULL
ORDER BY I.ITEM_ID DESC