def get_min_cost(cost,i):
    if cost[i] < cost[i+1]:
        return cost[i],i
    else:
        return cost[i+1],i+1
    
def minCostClimbingStairs(cost):
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
        min_cost,i = get_min_cost(cost,i)
        final_min_cost = final_min_cost + min_cost
        i=i+1
        
    return final_min_cost

t = minCostClimbingStairs([0,1,2,2])
print(t)