from turtle import *

screensize(10000,10000)
tracer(0)
left(90)
k = 10

for i in range(2):
    forward(15*k)
    left(90)
    forward(20*k)
    left(90)
up()
right(90)
back(7*k)
left(90)
forward(9*k)
down()
for i in range(2):
    forward(17*k)
    right(90)
    forward(15*k)
    right(90)

up()
for x in range(-100,100):
    for y in range(-100,100):
        goto(x*k,y*k)
        dot(3,"red")

update()
exitonclick()
