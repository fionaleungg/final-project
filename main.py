import turtle
from turtle import Turtle, Screen
import time
import random

# global variables
random_start_1 = random.randrange(-130,130)

screen = Screen()
# draw = Turtle("turtle")
# draw.speed(-1)
# draw.hideturtle()

# screen
screen = turtle.Screen()
height = 300
width = 300
screen.setup(width, height)
screen.bgcolor("#bdd9d4")

# -------- intro --------
# intro text
intro = turtle.Turtle()
intro.hideturtle()
intro.color("#418579")
intro.penup()
intro.goto(-100, 85)
intro.write("welcome to the turtle game! in this game")
intro.penup()
intro.goto(-125, 70)
intro.write("you're a turtle who needs to eat the falling food.")
intro.penup()
intro.goto(-125, 55)
intro.write(" after 30 seconds you win! simple enough right?")
intro.penup()
intro.goto(-85, 40)
intro.color("#2a543c")
intro.write("note: trash are black circles and")
intro.penup()
intro.goto(-70, 25)
# make black squares or green squares as tricks
intro.write("the food are green circles")


# intro turtle
intro_turtle = Turtle("turtle")
intro_turtle.color("#99b09b")
intro_turtle.left(90)
# start button
start_button = turtle.Turtle()
start_button.hideturtle()
start_button.color("#b39c66")
start_button.penup()
start_button.goto(-25, -60)
start_button.pendown()

for x in range (2):
  start_button.forward(50)
  start_button.left(90)
  start_button.forward(22)
  start_button.left(90)

start_button.penup()
start_button.goto(-13, -54.5)
start_button.write("start!")

# -------- turtle game --------
# timer
def game_timer():
  turtle_timer = turtle.Turtle()
  turtle_timer.hideturtle()
  turtle_timer.color("#6abaae")
  turtle_timer.penup()
  turtle_timer.goto(130, 130)
  seconds = 31
  down_Y = 130
  while (seconds != 0):
    for i in range (seconds):
      seconds = seconds - 1
      time.sleep(1)
      turtle_timer.clear()
      turtle_timer.write(seconds)
      while (down_Y != -146):
        trash = Turtle("circle")
        trash.penup()
        trash.showturtle()
        trash.goto(random_start_1, down_Y)
        time.sleep(1)
        trash.hideturtle()
        down_Y -= 23


# functionalizing the start button
def start_click(x, y):
  if (-24 < x < 25 and -60 < y < -39):
    start_button.clear()
    intro.clear()
    intro_turtle.hideturtle()
    game_timer()
    # draw.showturtle()

turtle.onscreenclick(start_click, 1)
# listening for mouse events
turtle.listen
# done keeps window from disappearing quickly
turtle.done()

# # -------- winner drawing --------
# # dragging
# def dragging (x, y):
#   draw.ondrag(None)
#   # pointing the cursor toward x, y
#   draw.setheading(t.towards(x, y))
#   draw.goto(x, y)
#   # if you continue to drag, it will continue to call the dragging function
#   draw.ondrag(dragging)

# def right_click(x, y):
#   draw.clear()

# def main():
#   turtle.listen()
#   draw.ondrag(dragging)
#   # 1: left click, 2: scroller click, 3: right click
#   turtle.onscreenclick(right_click, 3)
#   screen.mainloop()

# # main()