import turtle
from PIL import Image
img = Image.open("corpo.png")
img = img.resize((50, 50))
img.save("corpo.png")
t = turtle.Turtle()
s = turtle.Screen()
t.speed(0)
t.shape("turtle")
t.fillcolor("#01a2ff")
t.begin_fill()
for i in range(4):
    t.fd(100)
    t.right(90)
t.end_fill()
t.hideturtle()
turtle.done()