import turtle
import math

# Set up the Turtle Screen
screen = turtle.Screen()
screen.title("Wave Pattern Simulator")
screen.bgcolor("#4169E1")  # Set the background color to blue
screen.setup(width=800, height=600)

# Create a Turtle object
wave_turtle = turtle.Turtle()
wave_turtle.speed(0)  # Fastest drawing speed
wave_turtle.color("white")  # Set the color of the dots to white

# Function to draw wave pattern
def draw_wave_pattern():
    wave_turtle.penup()

    for y in range(-300, 300, 20):  # Grid height
        for x in range(-400, 400, 20):  # Grid width
            height = math.sin(math.radians(x)) * math.cos(math.radians(y))  # Calculate wave height
            wave_turtle.goto(x, y + height * 10)  # Adjust multiplier for wave amplitude
            wave_turtle.dot(3)  # Draw a small dot representing the wave peak/trough

    # Save the drawing
    screen.getcanvas().postscript(file="wave_pattern.eps")

# Draw the wave pattern
draw_wave_pattern()

# Hide the turtle and complete the drawing
wave_turtle.hideturtle()

# Convert .eps file to .png
try:
    from PIL import Image
    img = Image.open("wave_pattern.eps")
    img.save("wave_pattern.png")
except ImportError:
    print("PIL library not found. Image saved as wave_pattern.eps")

# Close the Turtle graphics window on click
screen.exitonclick()
