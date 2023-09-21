# import turtle module
import turtle as turtle
import random

# create turtle object
painter = turtle.Turtle()

painter.speed('fastest')

# Background
painter.fillcolor("#7b9db3")
painter.begin_fill()
painter.penup()
painter.left(90)
painter.forward(200)
painter.pencolor("black")
painter.pendown()

painter.left(90)
painter.forward(200)
painter.circle(20, 90)

painter.forward(400)
painter.circle(20, 90)
painter.forward(400)
painter.circle(20, 90)
painter.forward(400)
painter.circle(20, 90)
painter.forward(200)
painter.end_fill()
painter.penup()
painter.home()

# Function to create board
board_size = 13
def board():
    painter.begin_fill()
    painter.left(180)
    painter.forward(325)
    painter.right(120)
    painter.forward(board_size)
    painter.right(60)
    painter.forward(325)
    painter.end_fill()

# Board 1 & 2 - Blue
painter.penup()
painter.right(90)
painter.forward(240)
painter.left(90)
painter.forward(75)
painter.fillcolor("#5d7592")
painter.pendown()

painter.begin_fill()
painter.left(120)
painter.forward(325)
painter.right(120)
painter.forward(board_size)
painter.right(60)
painter.forward(325)
painter.end_fill()

painter.begin_fill()
painter.left(180)
painter.forward(325)
painter.right(120)
painter.forward(board_size)
painter.right(60)
painter.forward(325)
painter.end_fill()

# Board 3 & 4 - Purple
painter.fillcolor("#88789c")
board()
board()

# Board 5 & 6- Yellow
painter.fillcolor("#948760")
board()
board()

# Board 7 & 8 - Red
painter.fillcolor("#985450")
board()
board()

# Board 9 & 10 - Green
painter.fillcolor("#687468")
board()
board()

# Board 11 & 12 - Purple
painter.fillcolor("#746a80")
board()
board()

# Board 13 - Brown
painter.fillcolor("#8d736c")
board()

# Board 14 - Brown
painter.begin_fill()
painter.left(180)
painter.forward(325)
painter.right(120)
painter.forward(board_size)
painter.right(60)
painter.forward(250)
painter.end_fill()

# Cut
painter.fillcolor("white")
painter.begin_fill()
painter.penup()
painter.right(30)
painter.forward(65)
painter.right(90)
painter.forward(20)
painter.right(180)
painter.circle(20, 90)
painter.right(180)
painter.forward(20)
painter.left(90)
painter.forward(50)
painter.end_fill()

## Side
# Edge of board to give 3D effect
painter.goto(-87.50,41.46)
painter.right(90)
painter.fillcolor("#5d7592")
painter.begin_fill()
painter.pendown()
painter.forward(5)
painter.left(30)
painter.forward(318)
painter.end_fill()

# Side of boardwalk
painter.penup()
painter.goto(-87.50,41.46)
painter.right(30)
painter.pendown()
painter.forward(5)
painter.left(30)
painter.fillcolor("black")
painter.begin_fill()
painter.forward(10)
painter.right(30)
painter.forward(25)
painter.left(30)
painter.forward(280)
painter.left(60)
painter.forward(14)
painter.left(120)
painter.forward(310)
painter.end_fill()

# Re-outline to crisp edges
painter.penup()
painter.home()
painter.left(90)
painter.forward(200)
painter.pencolor("black")
painter.pendown()

painter.left(90)
painter.forward(200)
painter.circle(20, 90)

painter.forward(400)
painter.circle(20, 90)
painter.forward(400)
painter.circle(20, 90)
painter.forward(400)
painter.circle(20, 90)
painter.forward(200)
painter.penup()
painter.home()

# Function that makes waves
def waves(wave_amount):
    loop = 1
    while loop != wave_amount:
        circle_radius = random.randint(7, 14)
        painter.circle(circle_radius, 180)
        loop = loop + 1
        painter.right(180)

# First Waves
painter.left(90)
painter.forward(150)
painter.left(90)
painter.forward(150)
painter.left(90)
painter.pendown()
waves(15)

# Second Waves
painter.penup()
painter.forward(50)
painter.right(90)
painter.forward(150)
painter.left(90)
painter.pendown()
waves(7)

# Third Waves
painter.penup()
painter.goto((-190.00,-100.00))
painter.pendown()
waves(7)

# Letter Functions - https://github.com/adityadroid/Alphabeter/blob/master/withGUI.py
def letter(letter_name: str):
    if letter_name == "B":
        painter.left(90)
        painter.forward(50)
        painter.right(90)
        painter.forward(25)
        painter.right(90)
        painter.forward(25)
        painter.right(90)
        painter.forward(25)
        painter.right(180)
        painter.forward(25)
        painter.right(90)
        painter.forward(25)
        painter.right(90)
        painter.forward(25)
        painter.left(180)
        painter.forward(25)

    elif letter_name == "C":
        painter.forward(25)
        painter.left(180)
        painter.forward(25)
        painter.right(90)
        painter.forward(50)
        painter.right(90)
        painter.forward(25)
        painter.right(90)
        painter.penup()
        painter.forward(50)
        painter.pendown()
        painter.left(90)

    elif letter_name == "D":
        painter.forward(25)
        painter.left(180)
        painter.forward(25)
        painter.right(90)
        painter.forward(50)
        painter.right(90)
        painter.forward(25)
        painter.right(90)
        painter.forward(50)
        painter.left(90)

    elif letter_name == "E":
        painter.forward(25)
        painter.left(180)
        painter.forward(25)
        painter.right(90)
        painter.forward(25)
        painter.right(90)
        painter.forward(25)
        painter.right(180)
        painter.forward(25)
        painter.right(90)
        painter.forward(25)
        painter.right(90)
        painter.forward(25)
        painter.right(90)
        painter.penup()
        painter.forward(50)
        painter.pendown()
        painter.left(90)

    elif letter_name == "I":
        painter.forward(25)
        painter.left(180)
        painter.forward(12.5)
        painter.right(90)
        painter.forward(50)
        painter.left(90)
        painter.forward(12.5)
        painter.left(180)
        painter.forward(25)
        painter.right(90)
        painter.penup()
        painter.forward(50)
        painter.pendown()
        painter.left(90)

    elif letter_name == "L":
        painter.left(90)
        painter.forward(50)
        painter.left(180)
        painter.forward(50)
        painter.left(90)
        painter.forward(25)

    elif letter_name == "M":
        painter.left(90)
        painter.forward(50)
        painter.right(135)
        painter.forward(27.95)
        painter.left(90)
        painter.forward(27.95)
        painter.right(135)
        painter.forward(50)
        painter.left(90)

    elif letter_name == "O":
        painter.left(90)
        painter.forward(2.5)
        painter.forward(45)
        painter.right(45)
        painter.forward(3.535)
        painter.right(45)
        painter.forward(20)
        painter.right(45)
        painter.forward(3.535)
        painter.right(45)
        painter.forward(45)
        painter.right(45)
        painter.forward(3.535)
        painter.right(45)
        painter.forward(20)
        painter.right(45)
        painter.forward(3.535)
        painter.right(180)
        painter.forward(3.535)
        painter.left(45)
        painter.forward(20)
        painter.forward(2.5)

    elif letter_name == "U":
        painter.forward(2.5)
        painter.left(135)
        painter.forward(3.535)
        painter.right(45)
        painter.forward(47.5)
        painter.left(180)
        painter.forward(47.5)
        painter.left(45)
        painter.forward(3.535)
        painter.left(45)
        painter.forward(20)
        painter.left(45)
        painter.forward(3.535)
        painter.left(45)
        painter.forward(47.5)
        painter.left(180)
        painter.forward(47.5)
        painter.right(45)
        painter.forward(3.535)
        painter.left(135)
        painter.forward(2.5)
    
    else:
        print("ERROR: Letter requested not found")

# Letters
painter.penup()
painter.home()
painter.left(90)
painter.forward(225)
painter.left(90)
painter.forward(185)
painter.left(180)

painter.pendown()
painter.pensize(2)

letters = ["M", "E", "L", "O", "D", "I", "C", "B", "L", "U", "E"]
for name in letters:
    letter(letter_name=name)
    painter.penup()
    # gaps between letters
    if name == "C":
        painter.forward(20)
    else:
        painter.forward(5)
    painter.pendown()


painter.hideturtle()

# create screen object and make it persist
wn = turtle.Screen()
wn.mainloop()