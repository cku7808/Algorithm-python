-- 코드를 입력하세요
WITH RC AS (
    SELECT MEMBER_ID, COUNT(MEMBER_ID) AS REVIEW_COUNT
    FROM REST_REVIEW
    GROUP BY MEMBER_ID
    ORDER BY REVIEW_COUNT DESC
    LIMIT 1
)
SELECT MP.MEMBER_NAME, RR.REVIEW_TEXT, DATE_FORMAT(RR.REVIEW_DATE, "%Y-%m-%d") AS REVIEW_DATE
FROM MEMBER_PROFILE AS MP
INNER JOIN REST_REVIEW AS RR
ON MP.MEMBER_ID = RR.MEMBER_ID
INNER JOIN RC
ON RR.MEMBER_ID = RC.MEMBER_ID
ORDER BY REVIEW_DATE, REVIEW_TEXT



