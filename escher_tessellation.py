import turtle

def draw_square(t, size):
    """Draws a square with the given size."""
    # Loop to draw four sides of the square
    for _ in range(4):
        t.forward(size)  # Move turtle forward by the size specified
        t.right(90)      # Turn turtle right by 90 degrees

def tessellate_square(t, size, rows, cols):
    """Creates a tessellation pattern of squares."""
    # Loop through each row
    for row in range(rows):
        # Loop through each column in the current row
        for col in range(cols):
            draw_square(t, size)  # Draw a square at the current position
            t.forward(size)       # Move to the next position (right side)
        # Move back to the start of the row and then move down one row
        t.backward(cols * size)  # Move back to the beginning of the row
        t.right(90)              # Turn right to face downwards
        t.forward(size)          # Move down to the next row
        t.left(90)               # Turn left to face the start of the new row

def setup_turtle():
    """Sets up the turtle environment."""
    t = turtle.Turtle()        # Create a turtle object
    t.speed('fastest')         # Set the drawing speed to the fastest
    screen = turtle.Screen()   # Create a screen for the turtle
    screen.bgcolor('white')    # Set the background color of the screen
    t.penup()                  # Lift the pen up to move without drawing
    t.goto(-200, 200)          # Move the turtle to the starting position
    t.pendown()                # Put the pen down to start drawing
    return t, screen

def main():
    t, screen = setup_turtle()
    # Create a tessellation of squares with specified size and grid dimensions
    tessellate_square(t, 40, 10, 10)  
    screen.mainloop()  # Enter the main loop to display the window

# Ensures that this script runs only when it is executed as the main program
if __name__ == "__main__":
    main()
