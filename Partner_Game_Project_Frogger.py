

import turtle
import random
from math import *
from random import randint

t = turtle
t.setup(600, 400)
t.title("Frogger")

#frog
frog = t.Turtle()
frog.penup()
frog.shape("turtle")
frog.color("green")
frog.left(90)
frog.speed(0)
frog.setpos(0, -170)

#obtacles
obstlist = []
directions = []
for i in range(0, 10):
	blocks = t.Turtle()
	blocks.penup()
	blocks.shape("square")
	blocks.color("black")
	blocks.speed(0)
	blocks.setpos(randint(-300, 300), -140 + i * 40)
	obstlist.append(blocks)
	directions.append(1 - 2 * randint(0, 1))

print(directions)


def start():
	while True:
		i = 0
		(frogx, frogy) = frog.pos()
		for blocks in obstlist:
			(carx, cary) = blocks.pos()
			carx += 5 * directions[i]
			i += 1
			print(frogy)
			if carx < -310:
				carx = 300
			if carx > 310:
				carx = -300
			if abs(carx - frogx) < 20 and abs(cary - frogy) < 20:
				t.onkey(None, "Up")
				t.onkey(None, "Down")
				t.onkey(None, "Left")
				t.onkey(None, "Right")
				t.write("****YOU**LOSE****", align="center", font=("Arial", 22, "normal"))
				t.hideturtle()
				return
			elif frogy == 230:
				t.onkey(None, "Up")
				t.onkey(None, "Down")
				t.onkey(None, "Left")
				t.onkey(None, "Right")
				t.write("****YOU**WIN****", align="center", font=("Arial", 22, "normal"))
				t.hideturtle()
				return
			else:
				blocks.goto(carx, cary)

def up_():
	(frogx, frogy) = frog.pos()
	if frogy + 40 > -180:
		frog.goto(frogx, frogy  + 40)

def down_():
	(frogx, frogy) = frog.pos()
	if frogy - 40 > -180:
		frog.goto(frogx, frogy  - 40)

def left_():
	(frogx, frogy) = frog.pos()
	if frogx - 40 > -280:
		frog.goto(frogx - 40, frogy)

def right_():
	(frogx, frogy) = frog.pos()
	if frogy + 40 < 280:
		frog.goto(frogx + 40, frogy)


t.listen()
t.onkey(left_, "Left")
t.onkey(right_, "Right")
t.onkey(up_, "Up")
t.onkey(down_, "Down")
start()
t.mainloop()

