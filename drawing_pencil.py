# def jk():
#     return "Jose"
#
# var=jk()
# var2=jk
#
# print(var)
# print (var2)
# ================================

import turtle as tu

def forwards():
    biggie.forward(10)

def backwards():
    biggie.backward(10)

def clockwise():
    biggie.right(5)

def counter_clockwise():
    biggie.left(10)

def cc():
    biggie.clear()
    biggie.penup()
    biggie.home()
    biggie.pendown()

biggie=tu.Turtle()
screen=tu.Screen()

screen.listen() #this is the main method that tells the code to listen to the keys entered below.

screen.onkey(fun=forwards,key="w")
screen.onkey(fun=backwards,key="s")
screen.onkey(fun=clockwise,key="a")
screen.onkey(fun=counter_clockwise,key="d")
screen.onkey(fun=cc,key="c")


screen.exitonclick()

