# This program makes koch curves
# It's complexity is O(4^n)
from turtle import *
  
def drawSegment(level, distance):
    if level == 0:
        forward(distance)
        return 
    else:
        drawSegment(level - 1, distance/3)
        left(60)
        drawSegment(level - 1, distance/3)
        left(-120)
        drawSegment(level - 1, distance/3)
        left(60)
        drawSegment(level - 1, distance/3)
        

speed(0)
penup()

forward(-200)

pendown()
drawSegment(4, 300)

mainloop()