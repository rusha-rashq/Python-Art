import turtle
import math

# Create the turtle screen
window = turtle.Screen()
window.title("Rainbow Spiral")
window.bgcolor("black")

# Create a turtle
spiral = turtle.Turtle()
spiral.speed(0)

# Define the number of iterations and initial length
n = 180
length = 5

# Function to change color
def change_color(step):
    colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
    return colors[step % len(colors)]

# Function to draw the spiral
def draw_spiral(n, length):
    for step in range(n):
        # Change color
        spiral.color(change_color(step))
        
        # Draw forward and turn
        spiral.forward(length + step)
        spiral.right(45)
        
        # Increase the length slightly
        length += 0.5

# Draw the spiral
draw_spiral(n, length)

# Close the window on click
window.exitonclick()
