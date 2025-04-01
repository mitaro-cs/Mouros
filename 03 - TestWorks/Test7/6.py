from turtle import *

screensize(1000,1000)
tracer(0)
left(90)
k = 10

for i in range(3):
    down()
    for i in range(2):
        forward(10 * k)
        right(90)
        forward(10 * k)
        right(90)
    up()
    forward(5 * k)
    right(90)
    forward(5 * k)
    left(90)

up()
for x in range(-100,100):
    for y in range(-100,100):
        goto(x*k,y*k)
        dot(3, "red")

update()
exitonclick()