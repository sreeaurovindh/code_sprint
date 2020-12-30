Title : Group by vs Partion By 
Date : Sep 11, 2020 9:29:47 AM
Category :
Concepts: #GroupBy #PartitionBy
External Link : 


## Group by 

1. Reduces the no. of records
2. In select we need to use only columns which are used in group by. but we can use aggregate functions.
3. In filter condition we need to use having clause instead of where clause.

## Partition By

1. No. of records will not be reduced. Instead of that it will add one extra column.
2. In select we can use N no. of columns. No restrictions.
3. We can use where clause in filter condition apart from partition column.
 
 