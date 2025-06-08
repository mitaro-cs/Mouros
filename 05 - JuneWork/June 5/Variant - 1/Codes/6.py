from turtle import *
screensize(1000,1000)
tracer(0)
left(90)
k = 20

for i in range(8):
    forward(16*k)
    right(90)
    forward(22*k)
    right(90)

up()
forward(5*k)
right(90)
forward(5*k)
left(90)
down()

for i in range(8):
    forward(52*k)
    right(90)
    forward(77*k)
    right(90)

up()
for x in range(-100,100):
    for y in range(-100,100):
        goto(x*k,y*k)
        dot(3,"red")

update()
exitonclick()