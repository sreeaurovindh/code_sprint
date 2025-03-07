def test_my_code():
    work_a,work_b = [1,2,3] , [5,6,7,8]
    test_some_other_code(work_a,work_b)
    return work_a,work_b

def test_some_other_code(a,b):
    a.append(233)
    b.append(233)
    
a,b = test_my_code()
print(a,b)
