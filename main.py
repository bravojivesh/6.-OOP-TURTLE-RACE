
# set the window dimensions
# prompt display for input-- go through the doc
# create multiple instances.
# compare the entered word with the color of the turtle. So that whether the guess is correct can be determined.
# random steps ahead until edge of the box.
# how to know edge of the box?
#in the end display the result "you lose. The green turtle is the winner".
# so this means, we should retrieve the attribute of the instance of the turtle that completed the race first.

import turtle as tu
import random

screen1=tu.Screen()
screen1.setup(width=500,height=500)
ask= screen1.textinput(title="User input", prompt="Which turtle do you think will win?: ")

biggie, lima, mickey, keti, mizo, mouser=tu.Turtle(), tu.Turtle(),tu.Turtle(),tu.Turtle(), tu.Turtle(), tu.Turtle()

list=[biggie,lima,mickey,keti,mizo,mouser] #list of objects
color= ["red","green","blue","purple","orange","lime"]
eog=False #to end the game

x_cord=230
y_cord=150
i=0
winner_color=""

def set_loc_shape_starting_point():
    global x_cord,y_cord,i
    for x in list:
        x.shape("turtle")
        x.penup()
        x.color(color[i])
        x.goto(-x_cord,y_cord)
        i += 1
        y_cord-=50

def keep_moving():
    global eog, winner_color
    for x in list:
        x.forward(random.randint(0, 20))
        print(f"the color is :{x.color()[0]} and the x cordinate: {x.xcor()}")
        if x.xcor() > 200:
            print ("heeeeereeeeeeeeeeeeeeeeee")
            eog= True
            winner_color= x.color()[0]
            #retunr x.color()[0]    #This was my original. But in python return exits the func
            #tion immediately.
            break # the first match will exit the loop. Otherwise, it will run for all the values of biggie, lima etc.
            # (values of x)


if ask.strip()=="":
    eog=True

elif ask.strip()!="":
    set_loc_shape_starting_point()

    while eog==False:
        keep_moving()

    if ask==winner_color:
        print ("correct")
    else:
        print (f"Sorry, the winner is {winner_color} ")

screen1.exitonclick()

# biggie.goto(-x_cord,y_cord)

# if ask=="lol":

#     print ("yay")

