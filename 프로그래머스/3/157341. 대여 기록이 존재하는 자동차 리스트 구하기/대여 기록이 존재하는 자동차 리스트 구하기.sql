-- 코드를 입력하세요
SELECT DISTINCT C.CAR_ID
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY H
    LEFT JOIN CAR_RENTAL_COMPANY_CAR C ON H.CAR_ID = C.CAR_ID
WHERE START_DATE >= '2022-10-01' AND CAR_TYPE = '세단'
ORDER BY C.CAR_ID DESC