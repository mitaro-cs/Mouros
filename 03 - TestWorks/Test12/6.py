from turtle import *

screensize(10000,10000)
tracer(0)
left(90)
k = 7

up()
right(90)
right(45)
down()

for i in range(15):
    forward(20*k)
    right(90)
    forward(30*k)
    right(90)
    
up()
for x in range(-150,150):
    for y in range(-120,120):
        goto(x*k,y*k)
        dot(3,"red")

update()
exitonclick()
