-- 코드를 입력하세요
WITH PP AS(
    SELECT H.CAR_ID, CAR_TYPE, DAILY_FEE
    FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY H
        JOIN CAR_RENTAL_COMPANY_CAR C ON C.CAR_ID = H.CAR_ID
    WHERE CAR_TYPE = 'SUV' OR CAR_TYPE = '세단'
    GROUP BY H.CAR_ID
    HAVING MAX(DATE_FORMAT(END_DATE, '%Y-%m-%d')) < '2022-11-01' 
        OR MAX(DATE_FORMAT(START_DATE, '%Y-%m-%d')) > '2022-11-30' 
)

SELECT CAR_ID, P.CAR_TYPE
    , ROUND((DAILY_FEE*30)*((100-DISCOUNT_RATE)/100), 0) AS FEE
FROM PP AS P
    LEFT JOIN (
        SELECT * 
        FROM CAR_RENTAL_COMPANY_DISCOUNT_PLAN
        WHERE DURATION_TYPE LIKE '30%'
    ) AS D 
    ON P.CAR_TYPE = D.CAR_TYPE
HAVING FEE >= 500000 AND FEE < 2000000
ORDER BY FEE DESC, P.CAR_TYPE ASC, CAR_ID DESC



