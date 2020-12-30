# Min Cost Climbing Stairs

This following is the source code I wrote

```python
class Solution:
    def get_min_cost(self,cost,i):
        if cost[i] < cost[i+1]:
            return cost[i],i
        else:
            return cost[i+1],i+1

    def minCostClimbingStairs(self,cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        final_min_cost = i  = 0
        if len(cost) == 0:
            return 0
        elif len(cost) == 1:
            return cost[0]

        while i < (len(cost) -1):
            min_cost,i = self.get_min_cost(cost,i)
            final_min_cost = final_min_cost + min_cost
            i=i+1

        return final_min_cost
```

However,this code does not work. Why?

I figured out that the dynamic programming formulation for the above problem is 

```python
f[i] = cost[i] + min(f[i+1], f[i+2])
```

What you had calculated was 

```python
min_cost + min(cost[i],cost[i+1])
```



Clearly these above are not necessarily equal as you had missed the  actual cost  at each case. 





