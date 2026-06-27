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
def drawTriangle():
    for i in range(3):
        t.forward(100)
        t.left(120)
def draw6Angle():
    for i in range(6):
        t.forward(50)
        t.left(60)
def drawStar():
    for i in range(5):
        t.forward(60)
        t.left(72)
        t.forward(60)
        t.right(144)



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
def setYellow():
    t.color('yellow')
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
    t.begin_fill()
def endFill():
    t.end_fill()


t.ondrag(draw)
scr = t.getscreen()
scr.onscreenclick(move)
scr.onkey(setRed, "1")
scr.onkey(setGreen, "2")
scr.onkey(setBlue, "3")
scr.onkey(setWhite, "4")
scr.onkey(setBlack, "5")
scr.onkey(setYellow, "6")
scr.onkey(stepDown, "s")
scr.onkey(stepUp, "w")
scr.onkey(stepRight, "d")
scr.onkey(stepLeft, "a")
scr.onkey(startFill, "f")
scr.onkey(endFill, "e")
scr.onkey(clear, "q")
scr.onkey(drawCircle, "z")
scr.onkey(drawSq, "x")
scr.onkey(drawTriangle, "c")
scr.onkey(draw6Angle, "v")
scr.onkey(drawStar, "b")
scr.onkey(return0, "0")
scr.onkey(pensizeup, "Up")
scr.onkey(pensizedown, "Down")
scr.onkey(penup, "Right")
scr.onkey(pendown, "Left")

scr.listen()
