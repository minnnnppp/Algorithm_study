# -- 코드를 입력하세요
WITH TOP1 AS (
    SELECT MEMBER_ID
    FROM REST_REVIEW
    GROUP BY MEMBER_ID
    ORDER BY COUNT(DISTINCT REVIEW_ID) DESC
    LIMIT 1
)

SELECT MEMBER_NAME, REVIEW_TEXT, DATE_FORMAT(REVIEW_DATE, '%Y-%m-%d') AS REVIEW_DATE
FROM REST_REVIEW R
    LEFT JOIN MEMBER_PROFILE P ON R.MEMBER_ID = P.MEMBER_ID
WHERE R.MEMBER_ID IN (SELECT * FROM TOP1)
ORDER BY REVIEW_DATE ASC, REVIEW_TEXT ASC

