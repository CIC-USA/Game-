from tkinter import *
import time
import random
 
myTk = Tk()
myTk.title = ("Star Destroyer")
canvas = Canvas(myTk, width = 640, height = 480)
canvas.pack()
myTk.lift()
p = canvas.create_polygon(0, 0, -20, 40, 20 ,40, fill="gray")
d = canvas.create_rectangle(310, 370, 330, 400, fill="gray")
canvas.move(p,320, 390)
x = 320
y = 390
score = 0
alive = True
moveright = False
moveleft = False
islaser = False
speed = -2
L = -1
hitcount = 0
laserdelay = 0
is_star = False
B = -1
 
def keypress(event):
    global moveleft, moveright
    if event.keysym == "Left":
        moveleft = True
    if event.keysym == "Right":
        moveright = True
    if event.keysym == "space":
        makelaser()
 
 
def makelaser():
    global islaser, L, laserdelay
    if not islaser:
        L = canvas.create_rectangle(x-3, y-15, x+3, y+15, fill = "red")
        islaser = True
        laserdelay = 30
 
def keyrelease(event):
    global moveleft, moveright
    if event.keysym == "Left":
        moveleft = False
    if event.keysym == "Right":
        moveright = False
 
def movement():
    global x, y, islaser, laserdelay, p, d, speed
    if moveleft:
        canvas.move(p, -5, 0)
        canvas.move(d, -5, 0)
        x-=5
    if moveright:
        canvas.move(p, 5, 0)
        canvas.move(d, 5, 0)
        x +=5
    if islaser:
        canvas.move(L, 0, -20)
        laserdelay -=1
    if laserdelay == 0:
        canvas.delete(L)
        islaser = False
    if is_star:
        canvas.move(B, 0, speed)
 
 
 
