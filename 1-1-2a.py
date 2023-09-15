import turtle
import time

painter = turtle.Turtle()
def restart(type):
  print(f"⚠ Please enter a valid {type} ⚠")
  print("Restarting...")
  time.sleep(4)
  exit()

while True:
  try:
    color = input("\n\nColor:\n- ")
    radius = input("Circle Radius:\n- ")
    
    painter.pencolor(color)

    print("Drawing...")
    painter.circle(int(radius))
    print("Circle has been drawn")
  
  except turtle.TurtleGraphicsError:
    restart(type="color")
    
  except ValueError:
    restart(type="radius")

wn = turtle.Screen()
wn.mainloop()