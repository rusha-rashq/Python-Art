import random

def generate_starfield(width, height, star_frequency):
    """Generate a starfield pattern as a grid."""
    starfield = []
    for _ in range(height):
        row = []
        for _ in range(width):
            if random.random() < star_frequency:
                # Randomly choose a brightness character
                brightness = random.choice(['.', '+', '*', 'o', '@'])
                row.append(brightness)
            else:
                row.append(' ')
        starfield.append(''.join(row))
    return starfield

def save_starfield(starfield, filename):
    """Save the starfield pattern to a text file."""
    with open(filename, 'w') as file:
        for row in starfield:
            file.write(row + '\n')

def main():
    width, height = 80, 40  # Size of the starfield
    star_frequency = 0.1   # Probability of a star at a given point

    # Generate and save the starfield
    starfield = generate_starfield(width, height, star_frequency)
    save_starfield(starfield, 'starfield_pattern.txt')
    print("Starfield pattern saved to starfield_pattern.txt")

if __name__ == "__main__":
    main()
