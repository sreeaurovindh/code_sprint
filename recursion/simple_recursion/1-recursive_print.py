def recursive_print(num):
    if num < 1:
        return
    else:
        print("Prev Line: Test",num)
        recursive_print(num-1)
        print("End Line: Test",num)
        return


recursive_print(3)
