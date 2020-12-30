Title : Lag lead 
Date : Sep 11, 2020 10:42:32 AM
Category : 
Concepts: 
External Link : https://towardsdatascience.com/6-sql-tricks-every-data-scientist-should-know-f84be499aea5

```sql
SELECT 
		CUST_NAME,
		OUTSTANDING_AMT,
		lag(OUTSTANDING_AMT,1,0) over (order by OUTSTANDING_AMT desc) as lag_score
FROM CUSTOMER

```
