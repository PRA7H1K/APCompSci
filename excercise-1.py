import turtle
import time

painter = turtle.Turtle()

pencolor = input("What color would you like?")

painter.pensize(3)

painter.pencolor(pencolor)

painter.circle(50, 90, 20)
painter.circle(180, 180, 20)
painter.circle(270, 180, 20)
painter.circle(270, 90, 20)

painter.penup()
painter.home()
painter.pendown()

pencolor = input("What new color would you like?")

painter.pencolor(pencolor)

painter.circle(50, 90, 2)
painter.circle(180, 180, 3)
painter.circle(270, 270, 4)
painter.fillcolor("green")


wn = turtle.Screen()
wn.mainloop()