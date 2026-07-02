from turtle import *
while True:
    vhex = input("Enter your HEX code here: ").strip().lstrip("#")
    try:
        len(vhex) < 1
        if len(vhex) in [3, 6, 8] and all(c in "0123456789abcdefABCDEF" for c in vhex):
            break
        else:
            print("Invalid HEX code")
    except VallueError:
        vhex = input("Enter your HEX code here: ").strip().lstrip("#")



vcolor = "#" + vhex

t = Turtle()          
t.width(5)
t.color(vcolor)       
t.shape("circle")
t.width(1000)
t.forward(1)

#STGHECKER#
