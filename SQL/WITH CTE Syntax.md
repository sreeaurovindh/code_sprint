Title : With CTE
Date : Sep 11, 2020 10:21:56 AM
Category : 
Concepts: 
External Link : https://towardsdatascience.com/extra-4-sql-tricks-every-data-scientist-should-know-d3ed7cd7bc6c


```
WITH ag AS(
SELECT * FROM AGENTS
),
custdata AS(
SELECT * FROM CUSTOMER
)

SELECT  * 
FROM ag a
INNER JOIN custdata b
ON a.AGENT_CODE = b.AGENT_CODE

```
