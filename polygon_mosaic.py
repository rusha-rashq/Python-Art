import turtle
import random

# Function to draw a polygon
def draw_polygon(t, side_length, num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        t.forward(side_length)
        t.right(angle)

# Function to generate a random color
def random_color():
    return random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)

def main():
    screen = turtle.Screen()
    screen.bgcolor("white")
    screen.colormode(255)  # Use 255 RGB mode

    t = turtle.Turtle()
    t.speed('fastest')

    # Define the size of the mosaic and the size of each polygon
    mosaic_size = 10
    polygon_size = 40

    for x in range(-mosaic_size, mosaic_size):
        for y in range(-mosaic_size, mosaic_size):
            t.up()
            t.setpos(x * polygon_size, y * polygon_size)
            t.down()
            t.color(random_color())
            draw_polygon(t, polygon_size, 6)  # Drawing hexagons

    screen.mainloop()

if __name__ == "__main__":
    main()
