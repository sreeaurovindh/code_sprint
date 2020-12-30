# Revision Notes

#### Table of Contents

1. [General Things to Consider](#things)
2.  [Dictionary](#dict)
3. [Recursion](#recursion)



### <a name="things">General Things to consider</a>

#### <a name="dict">Dictionary</a>

```python
# Dictionary
from collections import defaultdict

#int dictionary
int_dict = defaultdict(int)

# list dictinary
list_dict = defaultdict(list)

# check if dictionary is present
if key in int_dict:
    print("Key Present")
else:
    print("Key absent")
    
# Get Keys and values as list
a= {0: 1, 2: 3, 3: 4, 4: 5}
all_keys = list(a.keys())
all_values = list(a.values())

# Enumerate key and values of dict
for key,value in enumerate(a):
    print(key,value)

```



#### <a name="recursion">Recursion</a> 

How to return a value in Python?

```python
def inorder(self,root,val):
    if root is None:
        return None
    if val is None:
        val = root.val
        elif val != root.val:
            return False
        left_val = self.inorder(root.left,val)
        right_val = self.inorder(root.right,val)

        if left_val is False or right_val is False:
            return False
        else:
            return True
        

```

