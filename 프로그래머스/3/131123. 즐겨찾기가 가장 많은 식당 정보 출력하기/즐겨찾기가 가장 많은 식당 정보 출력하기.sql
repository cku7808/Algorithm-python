SELECT FOOD_TYPE, REST_ID, REST_NAME, FAVORITES
FROM (SELECT FOOD_TYPE, REST_ID, REST_NAME, FAVORITES,
ROW_NUMBER() OVER(PARTITION BY FOOD_TYPE ORDER BY FAVORITES DESC) AS FAV_RANK
FROM REST_INFO) AS T
WHERE FAV_RANK = 1
ORDER BY FOOD_TYPE DESC
