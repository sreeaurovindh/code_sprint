#Given a non-negative int n, return the sum of its digits recursively (no loops). Note that mod (%) by 10 yields the rightmost digit (126 % 10 is 6), while divide (/) by 10 removes the rightmost digit (126 / 10 is 12).

#

def sumAlldigits(num):
   if num <10:
      return num
   else:
      return num%10 + sumAlldigits(num//10)

def sumAlldigits_iterative(num):
   num = abs(num)
   total = 0
   if num < 10:
      return num
   while num > 10:
      total += num %10
      num = num//10
   return total + num
   
       
    
    
    
print(sumAlldigits_iterative(-123))