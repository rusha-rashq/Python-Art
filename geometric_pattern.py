import turtle
import random

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create a turtle
t = turtle.Turtle()
t.speed(0)

def draw_polygon(sides, size):
    angle = 360 / sides
    for _ in range(sides):
        t.forward(size)
        t.right(angle)

def draw_star(sides, size):
    if sides % 2 != 0:
        angle = 180 - (180 / sides)
        for _ in range(sides):
            t.forward(size)
            t.right(angle)

def random_color():
    return (random.random(), random.random(), random.random())

def draw_shape(sides, size, shape_type):
    t.begin_fill()
    t.color(random_color())
    if shape_type == "polygon":
        draw_polygon(sides, size)
    elif shape_type == "star":
        draw_star(sides, size)
    t.end_fill()

# Draw multiple shapes
for i in range(20):
    x = random.randint(-200, 200)
    y = random.randint(-200, 200)
    t.penup()
    t.goto(x, y)
    t.pendown()
    
    sides = random.choice([3, 4, 5, 6, 7, 8])
    size = random.randint(20, 50)
    shape_type = random.choice(["polygon", "star"])
    
    draw_shape(sides, size, shape_type)

screen.mainloop()
