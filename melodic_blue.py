# import turtle module
import turtle as turtle

# create turtle object
painter = turtle.Turtle()
# turtle.speed(speed=0)

# painter.speed('normal')

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

# Board 1 - Blue
painter.fillcolor("#5d7592")
board_size = 13

painter.penup()
painter.right(90)
painter.forward(240)
painter.left(90)
painter.forward(75)

painter.pendown()
painter.begin_fill()
painter.left(120)
painter.forward(325)
painter.right(120)
painter.forward(board_size)
painter.right(60)
painter.forward(325)
painter.end_fill()

# Board 2 - Blue
painter.begin_fill()
painter.left(180)
painter.forward(325)
painter.right(120)
painter.forward(board_size)
painter.right(60)
painter.forward(325)
painter.end_fill()

# Board 3 - Purple
painter.fillcolor("#88789c")
painter.begin_fill()
painter.left(180)
painter.forward(325)
painter.right(120)
painter.forward(board_size)
painter.right(60)
painter.forward(325)
painter.end_fill()

# Board 4 - Purple
painter.begin_fill()
painter.left(180)
painter.forward(325)
painter.right(120)
painter.forward(board_size)
painter.right(60)
painter.forward(325)
painter.end_fill()

# Board 5 - Yellow
painter.fillcolor("#948760")
painter.begin_fill()
painter.left(180)
painter.forward(325)
painter.right(120)
painter.forward(board_size)
painter.right(60)
painter.forward(325)
painter.end_fill()

# Board 6 - Yellow
painter.begin_fill()
painter.left(180)
painter.forward(325)
painter.right(120)
painter.forward(board_size)
painter.right(60)
painter.forward(325)
painter.end_fill()

# Board 7 - Red
painter.fillcolor("#985450")
painter.begin_fill()
painter.left(180)
painter.forward(325)
painter.right(120)
painter.forward(board_size)
painter.right(60)
painter.forward(325)
painter.end_fill()

# Board 8 - Red
painter.begin_fill()
painter.left(180)
painter.forward(325)
painter.right(120)
painter.forward(board_size)
painter.right(60)
painter.forward(325)
painter.end_fill()

# Board 9 - Green
painter.fillcolor("#687468")
painter.begin_fill()
painter.left(180)
painter.forward(325)
painter.right(120)
painter.forward(board_size)
painter.right(60)
painter.forward(325)
painter.end_fill()

# Board 10 - Green
painter.begin_fill()
painter.left(180)
painter.forward(325)
painter.right(120)
painter.forward(board_size)
painter.right(60)
painter.forward(325)
painter.end_fill()

# Board 11 - Green
painter.fillcolor("#746a80")
painter.begin_fill()
painter.left(180)
painter.forward(325)
painter.right(120)
painter.forward(board_size)
painter.right(60)
painter.forward(325)
painter.end_fill()

# Board 12 - Green
painter.begin_fill()
painter.left(180)
painter.forward(325)
painter.right(120)
painter.forward(board_size)
painter.right(60)
painter.forward(325)
painter.end_fill()

# Board 13 - Green
painter.fillcolor("#8d736c")
painter.begin_fill()
painter.left(180)
painter.forward(325)
painter.right(120)
painter.forward(board_size)
painter.right(60)
painter.forward(325)
painter.end_fill()

# Board 14 - Green
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
# Edge
painter.goto(-87.50,41.46)
painter.right(90)
painter.fillcolor("#5d7592")
painter.begin_fill()
painter.pendown()
painter.forward(5)
painter.left(30)
painter.forward(318)
painter.end_fill()

# Bottom
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

# Re-outline
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

painter.hideturtle()

# create screen object and make it persist
wn = turtle.Screen()
wn.mainloop()