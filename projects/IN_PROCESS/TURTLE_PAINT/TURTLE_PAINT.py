from turtle import *
step = 15
t=Turtle()
t.color("black")
t.shape("circle")
t.width(5)
t.pendown()
t.speed(100)

def move(x,y):
    t.penup()
    t.goto(x, y)
    t.pendown()
#SPECIAL#
def clear():
    t.clear()
#SHAPES#
def drawCircle():
    t.circle(50)
def drawSq():
    for i in range(4):
        t.forward(50)
        t.left(90)
#CORDINATES#
def return0():
    t.penup()
    t.goto(0,0)
    t.pendown()

#PENSIZE#
def pensizeup():
    t.width(t.width() + 10)

def pensizedown():
    t.width(t.width() - 10)

#PENUP/DOWN#
def penup():
    t.penup()

def pendown():
    t.pendown()


#COLOR#
def setRed():
    t.color("red")
def setGreen():
    t.color("Green")
def setBlue():
    t.color("Blue")
def setWhite():
    t.color("white")
def setBlack():
    t.color("black")
#GOTO#
def draw(x,y):
    t.goto(x,y)
###############
def stepDown():
    t.goto(t.xcor(), t.ycor()-step)
def stepUp():
    t.goto(t.xcor(), t.ycor()+step)
def stepRight():
    t.goto(t.xcor()+step, t.ycor())
def stepLeft():
    t.goto(t.xcor()-step, t.ycor())
#FILL#

def startFill():
    t.begin_fill
def endFill():
    t.end_fill

#SPEED#

def plusSpeed():
    t.speed = t.speed + 10
def downSpeed():
    t.speed = t.speed - 10


t.ondrag(draw)
scr = t.getscreen()
scr.onscreenclick(move)
scr.onkey(setRed, "r")
scr.onkey(setGreen, "g")
scr.onkey(setBlue, "b")
scr.onkey(setWhite, "w")
scr.onkey(setBlack, "m")
scr.onkey(stepDown, "Down")
scr.onkey(stepUp, "Up")
scr.onkey(stepRight, "Right")
scr.onkey(stepLeft, "Left")
scr.onkey(startFill, "f")
scr.onkey(endFill, "e")
scr.onkey(clear, "c")
scr.onkey(drawCircle, "1")
scr.onkey(drawSq, "2")
scr.onkey(return0, "0")
scr.onkey(pensizeup, "x")
scr.onkey(pensizedown, "z")
scr.onkey(penup, "s")
scr.onkey(pendown, "a")

scr.listen()
