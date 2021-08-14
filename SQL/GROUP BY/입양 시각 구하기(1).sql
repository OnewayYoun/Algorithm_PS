/*
보호소에서는 몇 시에 입양이 가장 활발하게 일어나는지 알아보려 합니다.
09:00부터 19:59까지, 각 시간대별로 입양이 몇 건이나 발생했는지 조회하는 SQL문을 작성해주세요.
이때 결과는 시간대 순으로 정렬해야 합니다.
*/

-- 코드를 입력하세요
SELECT HOUR(datetime) AS HOUR, COUNT(*) AS COUNT
FROM animal_outs
-- 둘다 맞음
--WHERE 19 >= HOUR(datetime) AND HOUR(datetime) >= 9
--WHERE HOUR(datetime) BETWEEN 9 AND 19
GROUP BY HOUR(datetime)
-- 둘다 맞음
HAVING 19 >= HOUR AND HOUR >= 9
--HAVING HOUR BETWEEN 9 AND 19
ORDER BY HOUR(datetime)
# select * from animal_outs