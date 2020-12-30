# Buy and Sell Stock

```python
def maxProfit(self, prices):
"""
:type prices: List[int]
:rtype: int
"""

max_profit = 0
if len(prices) <= 1:
    return max_profit

min_uptil = prices[0]
for i in range(1,len(prices)):
    curr_profit = prices[i] - min_uptil
    if curr_profit > max_profit:
        max_profit = curr_profit
    min_uptil = min(min_uptil,prices[i])
return max_profit
```

