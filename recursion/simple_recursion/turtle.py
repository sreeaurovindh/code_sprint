import turtle

def tree_fractal(branch_len,t):
    if branch_len > 5:
        print(branch_len)
        t.forward(branch_len)
        t.right(20)
        tree_fractal(branch_len - 15,t)
        t.left(40)
        tree_fractal(branch_len -15 ,t)
        t.right(20)
        t.backward(branch_len)

t = turtle.Turtle()
win = turtle.Screen()
t.left(90)
t.up()
t.backward(100)
t.down()
t.color("green")
tree_fractal(80,t)
win.exitonclick()

def printMe(count):
    if count > 0:
        print("statement 1",count)
        printMe(count - 1 )
        print("Statement 2",count)
        # printMe(count -1)
        # print("Statment 3",count)

printMe(3)
