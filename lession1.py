
from turtle import *

#we want to paint a hause

#step 1: draw a square
width(7)
speed(40)
color("purple")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90) 
#and of square

#drawing a door

forward(70)
color("yellow")
begin_fill()
left(90)
forward(120)  #heightof the door
right(90)
forward(60)
right(90)
forward(120)
end_fill()
#and of door
penup()      #roof
goto(200,200)
pendown()


color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()
#and of roof

#window
color("blue")
begin_fill()
penup()
goto(20,150)
pendown()
left(120)
forward(50)
left(90)
forward(40)
left(90)
forward(50)
left(90)
forward(40)
end_fill()


begin_fill()
penup()
goto(180,150)
pendown()
left(180)
forward(40)
left(90)
forward(50)
left(90)
forward(40)
left(90)
forward(50)
end_fill()
exitonclick()




