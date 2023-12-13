import turtle
import random
import math

# Initialize the turtle
turtle.speed(0)
turtle.bgcolor("black")
turtle.hideturtle()

# Function to draw a spiral of shapes
def draw_spiral(radius, angle, shape_size, shape_sides, color):
    turtle.color(color)
    turtle.down()
    for _ in range(int(360 / angle)):
        turtle.forward(radius)
        turtle.begin_fill()
        draw_shape(shape_sides, shape_size)
        turtle.end_fill()
        turtle.backward(radius)
        turtle.right(angle)

# Function to draw a shape with a given number of sides
def draw_shape(sides, size):
    angle = 360 / sides
    for _ in range(sides):
        turtle.forward(size)
        turtle.right(angle)

# Function to change the color randomly
def random_color():
    return (random.random(), random.random(), random.random())

# Function to draw the kaleidoscope pattern
def kaleidoscope_pattern(iterations, shape_sides):
    for i in range(iterations):
        draw_spiral(radius=100 + i * 5, angle=10, shape_size=30, shape_sides=shape_sides, color=random_color())
        turtle.right(360 / iterations)

# Main execution
if __name__ == "__main__":
    turtle.tracer(0)  # Turns off the screen updates
    kaleidoscope_pattern(iterations=12, shape_sides=6)
    turtle.update()   # Updates the screen
    turtle.done()
