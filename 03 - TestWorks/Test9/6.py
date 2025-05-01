from turtle import *

screensize(10000,10000)
tracer(0)
left(90)
k = 25

up()
right(120)
down()
for i in range(10):
    forward(25*k)
    right(90)

up()
for x in range(-150,150):
    for y in range(-120,120):
        goto(x*k,y*k)
        dot(3,"red")

update()
exitonclick()
