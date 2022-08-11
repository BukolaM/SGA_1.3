SELECT *
FROM Bukola.managers_file;

SELECT (WORK_IN_COUNTRY) as COUNTRY,
	count(case when gender='Man' then 1 end) as Man,
	count(case when gender='Woman' then 1 end) as Woman,
	count(case when gender='Prefer not to answer' then 1 end) as Prefer_not_to_answer,
	count(case when gender='Non-Binary' then 1 end) as Non_Binary,
	count(*) as TOTAL_COUNT
from Bukola.managers_file
group by WORK_IN_COUNTRY

















