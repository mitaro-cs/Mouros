from turtle import *
screensize(10000,10000)
tracer(0)
left(90)
k = 7

for i in range(5):
   forward(30*k)
   right(90)
   forward(40*k)
   right(90)
up()
forward(20*k)
right(90)
forward(15*k)
right(90)
down()
for i in range(7):
   forward(10*k)
   right(90)

up()
for x in range(-100, 100):
   for y in range(-100, 100):
      goto(x*k,y*k)
      dot(3,"red")

update()
exitonclick()

