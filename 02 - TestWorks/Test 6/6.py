from turtle import *
screensize(10000,10000)
tracer(0)
k = 10
left(90)

for i in range(2):
   forward(23*k)
   left(90)
   back(27*k)
   left(90)
up()
back(5*k)
right(90)
forward(11*k)
left(90)
down()
for i in range(5):
   forward(26*k)
   right(90)
   forward(32*k)
   right(90)

up()
for x in range(-100,100):
   for y in range(-100,100):
      goto(x*k,y*k)
      dot(3,"red")

update()
exitonclick()
