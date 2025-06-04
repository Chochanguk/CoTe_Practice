# -- 코드를 작성해주세요
# SELECT ROUND(AVG(IF(LENGTH IS NULL ,10,LENGTH)),2)
# as AVERAGE_LENGTH
# FROM FISH_INFO;


# 10이하면 10으로 취급

SELECT ROUND(AVG(
        CASE 
            WHEN LENGTH IS NULL THEN 10
            WHEN LENGTH<=10 THEN 10
            ELSE LENGTH
        END)
             ,2) AS  AVERAGE_LENGTH -- 2짜리까지 반올림
FROM FISH_INFO;