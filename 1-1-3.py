import turtle as trtl

painter = trtl.Turtle()
painter.speed('fastest')

for line in range(18):
    painter.forward(20)
    painter.right(20)
    painter.stamp()

wn = trtl.Screen()
wn.mainloop()