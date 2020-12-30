Title : ROW_NUMBER() function 
Date : Sep 11, 2020 10:08:53 AM
Category : row_number
Concepts: #row_number
External Link : https://towardsdatascience.com/extra-4-sql-tricks-every-data-scientist-should-know-d3ed7cd7bc6c

## ROW_NUMBER() to return a subset of rows


```
 SELECT 
    ROW_NUMBER() OVER (PARTITION BY id_var ORDER BY num_var DESC) AS rownumber
 FROM cur_table 

```

## Length of consecutive days with ROW_NUMBER()

