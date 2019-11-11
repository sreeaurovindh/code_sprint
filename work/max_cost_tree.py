class output:
    def __init__(self,multipler,result):
        self.multiplier = multipler
        self.result = result

def mctFromLeafValues(arr):
    dp = [[None for i in range(len(arr))] for j in range(len(arr))]
    return solve(arr,dp,0,len(arr)-1).result

def solve(arr,dp,start,end):
    if dp[start][end] is not None:
        return dp[start][end]
    if start > end:
        return output(1,0)
    if start == end:
        return output(arr[start],0)
    minimum_val = None
    for i in range(start,end):
        left_node = solve(arr,dp,start,i)
        right_node = solve(arr,dp,i+1 ,end)
        final = output(max(left_node.multiplier,right_node.multiplier),left_node.result+ right_node.result+(left_node.multiplier*right_node.multiplier))
        if minimum_val is None or minimum_val.result > final.result:
            minimum_val = final
    dp[start][end] = minimum_val
    return minimum_val

print(mctFromLeafValues([6,2,4]))