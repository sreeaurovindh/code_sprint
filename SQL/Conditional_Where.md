Title :
Date : Sep 11, 2020 10:28:10 AM
Category : 
Concepts: 
External Link : 


## Conditional WHERE clause

Everyone knows the WHERE clause in SQL for subsetting. In fact, I find myself using conditional WHERE clause more often. With the toy table, for instance, we want only to keep the rows satisfying the following logic,
— if SEQ_VAR in (1, 2, 3) & diff(DATE_VAR2, DATE_VAR1)≥ 0
— elif SEQ_VAR in (4, 5, 6) & diff(DATE_VAR2, DATE_VAR1) ≥1
— else diff(DATE_VAR2, DATE_VAR1) ≥2
Now the conditional WHERE clause comes in handy,


```
-- 4) Conditional where clause
SELECT 
  DAT.ID_VAR,
  DAT.SEQ_VAR,
  DAT.NUM_VAR,
  DATE_VAR1, 
  DATE_VAR2,
  TRUNC(DATE_VAR2) - TRUNC(DATE_VAR1) AS LAG_IN_DATES
FROM 
  CURRENT_TABLE      DAT 
WHERE
  (TRUNC(DATE_VAR2) - TRUNC(DATE_VAR1)) >= CASE WHEN SEQ_VAR IN (1,2,3) THEN 0 WHEN SEQ_VAR IN (4,5,6) THEN 1 ELSE 2 END 
ORDER BY ID_VAR, SEQ_VAR

```

![Cond where](Images/20200911102918_cond_where.png)