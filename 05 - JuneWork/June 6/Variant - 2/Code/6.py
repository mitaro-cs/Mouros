from turtle import *
screensize(2000,2000)
tracer(0)
left(90)
k = 8

for i in range(3):
    forward(27*k)
    right(90)
    forward(12*k)
    right(90)
up()
forward(4*k)
right(90)
forward(6*k)
right(90)
down()
for i in range(4):
    forward(83*k)
    right(90)
    forward(77*k)
    right(90)
up()
for x in range(-150,150):
    for y in range(-150,150):
        goto(x*k,y*k)
        dot(4,"green")
update()
exitonclick()