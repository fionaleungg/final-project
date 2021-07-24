import turtle
from turtle import Turtle, Screen
import time
import random
from threading import Thread

# global variables
random_start_1 = random.randrange(-120, 120)
random_start_2 = random.randrange(-120, 120)
random_start_3 = random.randrange(-120, 120)
random_start_4 = random.randrange(-120, 120)
random_start_5 = random.randrange(-120, 120)
random_start_6 = random.randrange(-120, 120)
random_start_7 = random.randrange(-120, 120)
random_start_8 = random.randrange(-120, 120)

turtle_timer = turtle.Turtle()
turtle_timer.hideturtle()

trash1 = Turtle("circle")
trash1.hideturtle()
trash2 = Turtle("square")
trash2.hideturtle()
trash3 = Turtle("circle")
trash3.hideturtle()
trash4 = Turtle("circle")
trash4.hideturtle()
trash5 = Turtle("circle")
trash5.hideturtle()
trash6 = Turtle("square")
trash6.hideturtle()
trash7 = Turtle("circle")
trash7.hideturtle()
trash8 = Turtle("square")
trash8.hideturtle()

turtleX = 0
turtleY = 0
# turtle_timer = turtle.Turtle()
# turtle_timer.hideturtle()

col = ["green", "black", "gray"]
random_color= random.choice(col)

screen = Screen()

# screen
screen = turtle.Screen()
height = 300
width = 300
screen.setup(width, height)
screen.bgcolor("#ebe4c5")

# -------- intro --------
# intro text
intro = turtle.Turtle()
intro.hideturtle()
intro.color("#54401c")
intro.penup()
intro.goto(-100, 85)
intro.write("welcome to the turtle game! in this game")
intro.penup()
intro.goto(-125, 70)
intro.write("you're a turtle who needs to eat the falling food.")
intro.penup()
intro.goto(-125, 55)
intro.write(" after 10 seconds you win! simple enough right?")
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
# boundaries
def set_boundaries():
  boundaries = Turtle("turtle")
  boundaries.color("#1c1201")
  boundaries.hideturtle()
  boundaries.penup()
  boundaries.goto(-130, 130)
  boundaries.pendown()
  for x in range (2):
    boundaries.forward(270)
    boundaries.right(90)
    boundaries.forward(270)
    boundaries.right(90)

# turtle cursor
cursor = Turtle("turtle")
cursor.hideturtle()
cursor.color("#32a852")
cursor.speed(-1)
cursor.penup()
cursor.goto(90, 90)

def turtlecursor(x, y):
  cursor.speed(-1)
  cursor.ondrag(None)
  cursor.setheading(cursor.towards(x, y))
  cursor.penup()
  cursor.goto(x, y)
  cursor.ondrag(turtlecursor)
  
def main():
  turtle.listen()
  cursor.ondrag(turtlecursor)

def hide_all():
  trash1.hideturtle()
  trash2.hideturtle()
  trash3.hideturtle()
  trash4.hideturtle()
  trash5.hideturtle()
  trash6.hideturtle()
  trash7.hideturtle()
  trash8.hideturtle()
  turtle_timer.hideturtle()

# falling trash
# circle - black
def falling_trash_1():
  time.sleep(2)
  start_X1 = 130
  while (start_X1 != -146):
    trash1.color("black")
    trash1.penup()
    trash1.showturtle()
    trash1.goto(start_X1, random_start_1)
    if (cursor.xcor() == start_X1 and cursor.ycor() == random_start_1):
      hide_all()
    time.sleep(0.5)
    trash1.hideturtle()
    start_X1 -= 23
# square - green
def falling_trash_2():
  start_X2 = 130
  time.sleep(2)
  while (start_X2 != -146):
    trash2.color("green")
    trash2.penup()
    trash2.showturtle()
    trash2.goto(-(start_X2), random_start_2)
    if (cursor.xcor() == -(start_X2) and cursor.ycor() == random_start_2):
      hide_all()
    # print(cursor.xcor())
    # print(cursor.ycor())
    time.sleep(0.3)
    trash2.hideturtle()
    start_X2 -= 23
# circle - green
def falling_trash_3():
  down_Y3 = 130
  time.sleep(2)
  while (down_Y3 != -146):
    trash3.color("green")
    trash3.penup()
    trash3.showturtle()
    trash3.goto(random_start_3, -(down_Y3))
    if (cursor.ycor() == -(down_Y3) and cursor.xcor() == random_start_3):
      hide_all()
    time.sleep(0.7)
    trash3.hideturtle()
    down_Y3 -= 23
# circle - black
def falling_trash_4():
  down_Y4 = 130
  time.sleep(2)
  while (down_Y4 != -146):
    trash4.color("black")
    trash4.penup()
    trash4.showturtle()
    trash4.goto(random_start_4, down_Y4)
    if (cursor.ycor() == down_Y4 and cursor.xcor() == random_start_4):
      hide_all()
    time.sleep(0.5)
    trash4.hideturtle()
    down_Y4 -= 23
# circle - green
def falling_trash_5():
  down_Y5 = 130
  time.sleep(2)
  while (down_Y5 != -146):
    trash5.color("green")
    trash5.penup()
    trash5.showturtle()
    trash5.goto(random_start_5, down_Y5)
    if (cursor.ycor() == down_Y5 and cursor.xcor() == random_start_5):
      hide_all()
    time.sleep(0.5)
    trash5.hideturtle()
    down_Y5 -= 23
# square - green
def falling_trash_6():
  down_Y6 = 130
  time.sleep(2)
  while (down_Y6 != -146):
    trash6.color("green")
    trash6.penup()
    trash6.showturtle()
    trash6.goto(random_start_6, down_Y6)
    if (cursor.ycor() == down_Y6 and cursor.xcor() == random_start_6):
      hide_all()
    time.sleep(0.5)
    trash6.hideturtle()
    down_Y6 -= 23
# circle - black
def falling_trash_7():
  down_Y7 = 130
  time.sleep(2)
  while (down_Y7 != -146):
    trash7.color("black")
    trash7.penup()
    trash7.showturtle()
    trash7.goto(random_start_7, down_Y7)
    if (cursor.ycor() == down_Y7 and cursor.xcor() == random_start_7):
      hide_all()
    time.sleep(0.3)
    trash7.hideturtle()
    down_Y7 -= 23
# square - green2
def falling_trash_8():
  move_Y8 = 130
  time.sleep(2)
  while (move_Y8 != -146):
    trash8.color("green")
    trash8.penup()
    trash8.showturtle()
    trash8.goto(move_Y8, random_start_8)
    if (cursor.xcor() == move_Y8 and cursor.xcor() == random_start_8):
      hide_all()
    time.sleep(0.5)
    trash8.hideturtle()
    move_Y8 -= 23
# timer
def game_timer():
  turtle_timer.color("#1c1201")
  turtle_timer.penup()
  turtle_timer.goto(115, 100)
  seconds = 16
  for i in range (seconds):
    seconds = seconds - 1
    time.sleep(1)
    turtle_timer.clear()
    turtle_timer.write(seconds)
    if (seconds == 0):
      turtle_timer.goto(-15, -15)
      turtle_timer.write("congrats!")


# threads
t1 = Thread(target = game_timer)
t2 = Thread(target = falling_trash_1)
t3 = Thread(target = falling_trash_2)
t4 = Thread(target = falling_trash_3)
t5 = Thread(target = falling_trash_4)
t6 = Thread(target = falling_trash_5)
t7 = Thread(target = falling_trash_6)
t8 = Thread(target = falling_trash_7)
t9 = Thread(target = falling_trash_8)


# game logic

# functionalizing the start button
def start_click(x, y):
 
 
  if (-24 < x < 25 and -60 < y < -39):
    start_button.clear()
    intro.clear()
    intro_turtle.hideturtle()
    set_boundaries()
    t1.start() 
    t2.start() 
    t3.start() 
    t4.start() 
    t5.start() 
    t6.start() 
    t7.start() 
    t8.start() 
    t9.start() 
    cursor.showturtle()
    main()

    # draw.showturtle()

turtle.onscreenclick(start_click, 1)
# listening for mouse events
turtle.listen
# done keeps window from disappearing quickly
turtle.done()

#def check_eaten(trash):
 # x_cor = trash.xcor()
 # y_cor = trash.ycor()
 # if h.distance(trash) < 15:
 #   trash.hideturtle()
 #   print("You collided")
