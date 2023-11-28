-- 코드를 입력하세요
SELECT FLAVOR
FROM (
SELECT FH.FLAVOR AS FLAVOR, SUM(FH.TOTAL_ORDER) + SUM(J.TOTAL_ORDER) AS TOTAL
FROM FIRST_HALF AS FH
INNER JOIN JULY AS J
ON FH.FLAVOR = J.FLAVOR
GROUP BY FH.FLAVOR
ORDER BY TOTAL DESC
) AS a
LIMIT 3
