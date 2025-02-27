from turtle import *
screensize(10000,10000)
k = 25
tracer(0)
left (90)

for i in range(2):
   fd(8*k)
   rt(90)
   fd(18*k)
   rt(90)
up()
fd(4*k)
rt(90)
fd(10*k)
lt(90)
down()
for i in range(2):
   fd(17*k)
   rt(90)
   fd(7*k)
   rt(90)
up()
for x in range(-100,100):
   for y in range(-100,100):
      goto(x*k,y*k)
      dot(3,"red")

update()
exitonclick()

