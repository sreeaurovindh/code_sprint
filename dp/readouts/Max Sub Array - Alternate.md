 ## Maxium Sum Array - Alternate Elements

  The idea is to find the maxium sum of non consecutive elements in the array. 
  Expand the notes from
  [Stack Overflow](https://stackoverflow.com/questions/4487438/maximum-sum-of-non-consecutive-elements)
  [Educativeio](https://www.educative.io/collection/page/5642554087309312/5679846214598656/140002)

  ```python
  sum[0] = A[0]
  sum[1] = max(A[0],A[1])
  Sum[2] = max(Sum[0]+arr[2],Sum[1])
  Sum[3] = max(sum[1]+arr[3],sum[2])
  ...
  Sum[i] = max(Sum[i-2]+arr[i],Sum[i-1]) when i>=2
  ```

