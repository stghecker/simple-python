from turtle import * 
from random import randint
from random import sample
from time import sleep
finish = 200
def startRace(t,x,y,color):
    t.color(color)
    t.shape("turtle")
    t.speed(100)
    t.penup()
    t.goto(x,y)


t1 = Turtle()
t2 = Turtle()
t3 = Turtle()


startRace(t1, -200, -20, "red")
startRace(t2, -200, 20, "blue")
startRace(t3, -200, 60, "yellow")

sleep(1)

while t1.xcor() < finish and t2.xcor() < finish and t3.xcor() < finish:
    num1, num2, num3 = sample(range(1, 9), 3)
    t1.forward(num1)
    t2.forward(num2)
    t3.forward(num3)
sleep(1)

def dance(t):
   t.speed(15)
   t.left(randint(0, 90))
   j = 0
   while j < 8:          
       t.penup()
       t.goto(0, 0)
       t.pendown()
       i = 1
       while i < 32:
           t.forward(i)
           t.left(i/2+5)
           i += 1
       j += 1
   t.penup()
   t.goto(0, 0)
sleep(1)

max_x = max(t1.xcor(), t2.xcor(),t3.xcor())


if t1.xcor() == max_x:
   t2.hideturtle()
   t3.hideturtle()
   dance(t1)



if t2.xcor() == max_x:
   t1.hideturtle()
   t3.hideturtle()
   dance(t2)


if t3.xcor() == max_x:
   t1.hideturtle()
   t2.hideturtle()
   dance(t3)



#STGHECKER#
