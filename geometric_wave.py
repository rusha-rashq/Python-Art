import turtle
import random

# Set up the screen
screen = turtle.Screen()
screen.title("Geometric Wave Pattern")
screen.bgcolor("white")

# Create a turtle object
wave = turtle.Turtle()
wave.speed(0)

# Function to draw a circle with varying size and color
def draw_circle(size, color):
    wave.color(color)
    wave.begin_fill()
    wave.circle(size)
    wave.end_fill()

# Main drawing loop
for i in range(50):
    # Calculate size and color
    size = 20 + i * 5
    color = random.choice(["blue", "green", "red", "purple", "orange", "yellow"])
    
    # Position the turtle
    wave.penup()
    wave.goto(0, -size)
    wave.pendown()
    
    # Draw the circle
    draw_circle(size, color)

    # Rotate the turtle
    wave.left(10)

# Complete the drawing
wave.hideturtle()
screen.mainloop()
