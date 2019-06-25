#This program creates the Sierpinksi Triangle
#Its complexity is 3^n

from turtle import *

def triangle(level, top_point, left_point, right_point):
	if level == 0:
		penup()
		setpos(left_point)
		fill(True)
		pendown()
		for _ in range(3):
		    forward(right_point[0] - left_point[0])
		    left(120)
		
		fill(False)
		return

	left_mid = [((top_point[0] + left_point[0]) / 2), ((top_point[1] + left_point[1]) / 2)]
	right_mid = [((top_point[0] + right_point[0]) / 2), ((top_point[1] + right_point[1]) / 2)]
	bottom_mid = [((right_point[0] + left_point[0]) / 2), ((right_point[1] + left_point[1]) / 2)]

	triangle(level-1, top_point, left_mid, right_mid)
	triangle(level-1, left_mid, left_point, bottom_mid)
	triangle(level-1, right_mid, bottom_mid, right_point)

triangle(4, (60, 106.6), (10, 20), (110, 20))
mainloop()