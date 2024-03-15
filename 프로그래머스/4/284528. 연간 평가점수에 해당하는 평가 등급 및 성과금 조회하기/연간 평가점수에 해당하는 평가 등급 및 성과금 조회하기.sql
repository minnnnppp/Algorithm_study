-- 코드를 작성해주세요
WITH SCORES AS (
    SELECT EMP_NO, 
            CASE 
                WHEN AVG(SCORE) >= 96 THEN 'S'
                WHEN AVG(SCORE) >= 90 THEN 'A'
                WHEN AVG(SCORE) >= 80 THEN 'B'
                WHEN AVG(SCORE) < 80 THEN 'C'
            END AS 'GRADE'
    FROM HR_GRADE
    GROUP BY EMP_NO
)

SELECT S.EMP_NO, EMP_NAME, GRADE, 
        CASE 
            WHEN GRADE = 'S' THEN 0.2*SAL
            WHEN GRADE = 'A' THEN 0.15*SAL
            WHEN GRADE = 'B' THEN 0.1*SAL
            ELSE 0
        END AS 'BONUS'
FROM HR_EMPLOYEES H
    JOIN SCORES S ON H.EMP_NO = S.EMP_NO
ORDER BY S.EMP_NO
