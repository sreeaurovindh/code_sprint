Title : Finding Cumulative Sum
Date : Sep 11, 2020 10:24:56 AM
Category : 
Concepts: #Rows_Unbounded
External Link : https://towardsdatascience.com/6-sql-tricks-every-data-scientist-should-know-f84be499aea5

```
SELECT c.*,
SUM(OUTSTANDING_AMT) OVER (ORDER BY OUTSTANDING_AMT ROWS UNBOUNDED PRECEDING) AS CUM_SUM
FROM CUSTOMER c
```