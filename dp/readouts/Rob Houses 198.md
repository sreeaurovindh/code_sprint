Title :   
Date : Sep 5, 2020 12:20:14 PM  
Concepts:  #Top_down #Swap   
External Link : https://www.notion.so/Rob-Non-Consecutive-Houses-c929034b69474ebcbe9fda44f5914bc5  
Leetcode : https://leetcode.com/problems/house-robber/  

## **Algorithm**

It could be overwhelming thinking of all possibilities on which houses to rob.

A natural way to approach this problem is to work on the simplest case first.

Let us denote that:

> 1. f(k) = Largest amount that you can rob from the first k houses.

> 2. Ai = Amount of money at the ith house.

Let us look at the case `n = 1`, clearly *f*(1) = A1.

Now, let us look at `n = 2`, which *f*(2) = max(A1, A2).

For `n = 3`, you have basically the following two options:

1. Rob the third house, and add its amount to the first house's amount.
2. Do not rob the third house, and stick with the maximum amount of the first two houses.

Clearly, you would want to choose the larger of the two options at each step.

Therefore, we could summarize the formula as following:

> f(k) = max(f(k – 2) + Ak, f(k – 1))

We choose the base case as *f*(–1) = *f*(0) = 0, which will greatly simplify our code as you can see.

The answer will be calculated as *f*(*n*). We could use an array to store and calculate the result, but since at each step you only need the previous two maximum values, two variables are suffice.

```python
public int rob(int[] num) {
    int prevMax = 0;
    int currMax = 0;
    for (int x : num) {
        int temp = currMax;
        currMax = Math.max(prevMax + x, currMax);
        prevMax = temp;
    }
    return currMax;
}

```

**Complexity analysis**

- Time complexity : `O(n)` . Assume that  is the number of houses, the time complexity is `O(n)`
- Space complexity : `O(1)`