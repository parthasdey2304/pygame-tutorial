import pygame
import sys

# Initialize Pygame
pygame.init()

# Game settings
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
FPS = 60

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Create the game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pygame Learning")

# Game variables
clock = pygame.time.Clock()
running = True

# Player variables
player_width, player_height = 50, 50
player_x = SCREEN_WIDTH // 2 - player_width // 2
player_y = SCREEN_HEIGHT - player_height
player_speed = 5

# Main game loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Handle player movements
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed
    if keys[pygame.K_UP]:
        player_y -= player_speed
    if keys[pygame.K_DOWN]:
        player_y += player_speed

    # Prevent the player from moving outside the window
    player_x = max(0, min(player_x, SCREEN_WIDTH - player_width))
    player_y = max(0, min(player_y, SCREEN_HEIGHT - player_height))

    # Draw everything on the screen
    screen.fill(BLACK)

    # Draw player
    pygame.draw.rect(screen, RED, (player_x, player_y, player_width, player_height))

    # Draw shapes (e.g., circle, line, etc.)
    pygame.draw.circle(screen, GREEN, (100, 100), 30)
    pygame.draw.line(screen, BLUE, (200, 200), (300, 300), 3)

    # Display text
    font = pygame.font.SysFont(None, 30)
    text = font.render("Hello, Pygame!", True, WHITE)
    screen.blit(text, (10, 10))

    pygame.display.update()

    # Control the frame rate
    clock.tick(FPS)

# Quit Pygame
pygame.quit()
sys.exit()
