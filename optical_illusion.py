import turtle
import math

def draw_square(t, size):
    for _ in range(4):
        t.forward(size)
        t.right(90)

def draw_illusion():
    window = turtle.Screen()
    window.bgcolor("white")

    illusion = turtle.Turtle()
    illusion.speed(0)

    colors = ["red", "green", "blue", "orange", "purple", "yellow", "black"]

    size = 100
    for i in range(100):
        illusion.color(colors[i % len(colors)])
        draw_square(illusion, size)
        illusion.right(10)
        size += 2

    window.exitonclick()

draw_illusion()
