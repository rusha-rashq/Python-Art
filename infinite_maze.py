import turtle
import random
import time

# Initialize the Turtle Screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create a Turtle for drawing
maze_turtle = turtle.Turtle()
maze_turtle.speed(0)
maze_turtle.color("black")

# Define maze parameters
path_width = 20
turn_choices = [90, -90]

# Function to draw a segment of the maze
def draw_segment(length):
    maze_turtle.forward(length)
    maze_turtle.right(random.choice(turn_choices))

# Main loop to draw the maze
while True:
    draw_segment(path_width)
    time.sleep(0.1)  # Adjust speed of drawing here

# Keep the window open
turtle.done()
