import turtle
import random

# Function to draw a hexagon
def draw_hexagon(x, y, size, color):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color(color)
    turtle.begin_fill()
    for _ in range(6):
        turtle.forward(size)
        turtle.left(60)
    turtle.end_fill()

# Function to generate a random color
def random_color():
    return random.choice(['red', 'green', 'blue', 'yellow', 'purple', 'orange'])

# Main function to create the pattern
def main():
    screen = turtle.Screen()
    screen.setup(width=800, height=800)  # Set the window size

    turtle.speed(0)
    turtle.hideturtle()

    # Size of each hexagon
    hexagon_size = 30
    # Spacing between hexagons
    spacing = hexagon_size * 3 ** 0.5

    # Rows and columns of hexagons
    rows = 10
    columns = 10

    # Calculate the centering offset
    offset_x = -columns * spacing * 0.75
    offset_y = -rows * spacing * 0.5 / 2

    # Drawing the hexagons
    for row in range(rows):
        for col in range(columns):
            x = col * spacing * 1.5 + offset_x
            y = row * spacing - (col % 2) * spacing / 2 + offset_y
            draw_hexagon(x, y, hexagon_size, random_color())

    turtle.done()

if __name__ == "__main__":
    main()
