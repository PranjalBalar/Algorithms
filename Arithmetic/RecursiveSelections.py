# -*- coding: utf-8 -*-

#This program recursively selects a number between 1 and 10 
def select(index, choices, selections):
	if index == len(selections):
		return selections

	else:
		x = 1
		if index > 0:
			x = selections[index - 1] + 1

		for i in range(x, choices):
			selections[index] = i
			return select(index + 1, choices, selections)

s = [0] * 5
print select(0, 10, s)

