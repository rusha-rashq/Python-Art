import turtle
import random
import math

def random_color():
    """Generate a random RGB color."""
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

def draw_fermat_spiral(turns, dots_per_turn, scale_factor, dot_size):
    """Draw an enlarged Fermat's spiral with dots."""
    screen = turtle.Screen()
    screen.colormode(255)  # Use RGB color mode
    screen.screensize(2000, 2000)  # Increase the canvas size
    spiral = turtle.Turtle()
    spiral.speed(0)  # Fastest drawing speed
    spiral.penup()  # Don't draw lines
    spiral.hideturtle()  # Hide the turtle cursor
    screen.tracer(0)  # Turn off animation

    # Calculate the number of dots
    num_dots = turns * dots_per_turn

    for i in range(num_dots):
        angle = i / dots_per_turn * 2 * math.pi  # Convert dot number to radians
        r = math.sqrt(angle) * scale_factor  # Apply the Fermat's spiral formula and scale
        x = r * math.cos(angle)  # Polar to Cartesian conversion for x-coordinate
        y = r * math.sin(angle)  # Polar to Cartesian conversion for y-coordinate
        spiral.goto(x, y)
        spiral.dot(dot_size, random_color())  # Draw a larger dot with a random color
        if i % 100 == 0:  # Update the screen every 100 dots
            screen.update()

    screen.update()  # Ensure the final update if not divisible by 100
    screen.getcanvas().postscript(file="fermat_spiral.eps")  # Save as EPS
    screen.exitonclick()  # Close the window when clicked

# Adjust scale_factor and dot_size as needed
draw_fermat_spiral(turns=20, dots_per_turn=100, scale_factor=10, dot_size=5)
