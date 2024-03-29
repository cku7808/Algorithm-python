-- 코드를 입력하세요
SELECT 
YEAR(OS.SALES_DATE) AS YEAR,
MONTH(OS.SALES_DATE) AS MONTH,
COUNT(DISTINCT OS.USER_ID) AS PUCHASED_USERS,
ROUND(COUNT(DISTINCT UI.USER_ID) / (SELECT COUNT(DISTINCT USER_ID) FROM USER_INFO WHERE YEAR(JOINED) = "2021"),1) AS PUCHASED_RATIO
FROM USER_INFO AS UI
LEFT OUTER JOIN ONLINE_SALE AS OS
ON UI.USER_ID = OS.USER_ID
WHERE YEAR(UI.JOINED) = "2021" AND OS.USER_ID IS NOT NULL
GROUP BY YEAR, MONTH