import turtle
import random

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("navy")  # Set the background to navy blue
screen.setup(width=800, height=600)
screen.title("Starry Night Simulation")

# Create a turtle for drawing stars
star_turtle = turtle.Turtle()
star_turtle.hideturtle()
star_turtle.speed(0)  # Fastest drawing speed

def draw_star(x, y, size):
    """Function to draw a star at a given position and size."""
    star_turtle.penup()
    star_turtle.goto(x, y)
    star_turtle.pendown()
    star_turtle.dot(size, "white")

# Draw stars randomly
for _ in range(200):  # Number of stars
    x = random.randint(-400, 400)
    y = random.randint(-300, 300)
    size = random.randint(1, 6)  # Varying sizes for distance effect
    draw_star(x, y, size)

# Keep the window open
turtle.done()
