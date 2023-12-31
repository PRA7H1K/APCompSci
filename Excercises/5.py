#   a113_tower.py
#   Modify this code in VS Code to alternate the colors of the 
#   floors every three floors
import turtle as trtl

painter = trtl.Turtle()
painter.speed(0)
painter.pensize(5)

# starting location of the tower
x = -150
y = -150

# height of tower and a counter for each floor
num_floors = 45

# iterate
for floor in range(num_floors):
  # set placement and color of turtle
  painter.penup()
  painter.goto(x, y)
  painter.color("blue")
  y = y + 5 # location of next floor
   
  #draw the floor

  alternate = floor % 6
  if (alternate < 3):
    painter.color("grey")
  painter.pendown()
  painter.forward(50)

painter.hideturtle()

wn = trtl.Screen()
wn.mainloop()