/*
동물 보호소에 동물이 몇 마리 들어왔는지 조회하는 SQL 문을 작성해주세요.
*/

-- 코드를 입력하세요
SELECT COUNT(*) AS count
FROM animal_ins
WHERE animal_type IS NOT NULL