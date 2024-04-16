import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60
FRUIT_SIZE = 50
BOMB_SIZE = 50
FRUIT_SPEED = 5
BOMB_SPEED = 7
FRUIT_COLORS = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]  # Red, Green, Blue
BOMB_COLOR = (0, 0, 0)  # Black
FONT_SIZE = 36
SCORE_POSITION = (10, 10)

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Fruit Ninja")

# Fonts
font = pygame.font.Font(None, FONT_SIZE)

# Clock
clock = pygame.time.Clock()

# Lists to store fruits and bombs
fruits = []
bombs = []

# Score
score = 0

# Function to create a new fruit
def create_fruit():
    color = random.choice(FRUIT_COLORS)
    x = random.randint(0, WIDTH - FRUIT_SIZE)
    y = HEIGHT
    fruits.append({"rect": pygame.Rect(x, y, FRUIT_SIZE, FRUIT_SIZE), "color": color, "speed": FRUIT_SPEED})

# Function to create a new bomb
def create_bomb():
    x = random.randint(0, WIDTH - BOMB_SIZE)
    y = HEIGHT
    bombs.append({"rect": pygame.Rect(x, y, BOMB_SIZE, BOMB_SIZE), "color": BOMB_COLOR, "speed": BOMB_SPEED})

# Main game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill((255, 255, 255))

    # Check for fruit and bomb collisions with the bottom of the screen
    for fruit in fruits:
        if fruit["rect"].bottom <= 0:
            fruits.remove(fruit)
            create_fruit()
        else:
            fruit["rect"].move_ip(0, -fruit["speed"])

    for bomb in bombs:
        if bomb["rect"].bottom <= 0:
            bombs.remove(bomb)
            create_bomb()
        else:
            bomb["rect"].move_ip(0, -bomb["speed"])

    # Draw fruits and bombs
    for fruit in fruits:
        pygame.draw.ellipse(screen, fruit["color"], fruit["rect"])

    for bomb in bombs:
        pygame.draw.ellipse(screen, bomb["color"], bomb["rect"])

    # Display score
    score_text = font.render("Score: " + str(score), True, (0, 0, 0))
    screen.blit(score_text, SCORE_POSITION)

    # Update the display
    pygame.display.flip()

    # Limit frames per second
    clock.tick(FPS)

# Quit Pygame
pygame.quit()
