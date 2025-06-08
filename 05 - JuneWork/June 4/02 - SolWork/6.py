from turtle import *
screensize(1000,1000)
tracer(0)
left(90)
k = 20

right(90)
for i in range(7):
    right(45)
    forward(11*k)
    right(45)

up()
for x in range(-100,100):
    for y in range(-100,100):
        goto(x*k,y*k)
        dot(3,"red")

update()
exitonclick()