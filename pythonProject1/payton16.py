import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the screen
SCREEN_WIDTH = 1080
SCREEN_HEIGHT = 2400
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Simple Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)

# Player
player_img = pygame.Surface((50, 50))
player_img.fill(WHITE)
player_rect = player_img.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))



# Button dimensions and positions
BUTTON_SIZE = 150
BUTTON_MARGIN = 10
BUTTON_SPACING = BUTTON_SIZE + BUTTON_MARGIN
BUTTON_START_X = 450
BUTTON_START_Y = 1200

# Button colors
BUTTON_COLOR = (100, 100, 100)
BUTTON_ACTIVE_COLOR = (150, 150, 150)

# Buttons
up_button_rect = pygame.Rect(BUTTON_START_X, BUTTON_START_Y, BUTTON_SIZE, BUTTON_SIZE)
down_button_rect = pygame.Rect(BUTTON_START_X, BUTTON_START_Y + BUTTON_SPACING, BUTTON_SIZE, BUTTON_SIZE)
left_button_rect = pygame.Rect(BUTTON_START_X - BUTTON_SPACING, BUTTON_START_Y + BUTTON_SPACING, BUTTON_SIZE, BUTTON_SIZE)
right_button_rect = pygame.Rect(BUTTON_START_X + BUTTON_SPACING, BUTTON_START_Y + BUTTON_SPACING, BUTTON_SIZE, BUTTON_SIZE)

# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button
                if up_button_rect.collidepoint(event.pos):
                    player_rect.y -= 70
                elif down_button_rect.collidepoint(event.pos):
                    player_rect.y += 70
                elif left_button_rect.collidepoint(event.pos):
                    player_rect.x -= 70
                elif right_button_rect.collidepoint(event.pos):
                    player_rect.x += 70

    # Keep player within screen bounds
    player_rect.x = max(0, min(player_rect.x, SCREEN_WIDTH - player_rect.width))
    player_rect.y = max(0, min(player_rect.y, SCREEN_HEIGHT - player_rect.height))

    # Clear screen
    screen.fill(BLACK)

    # Draw player
    screen.blit(player_img, player_rect)

    # Draw buttons
    pygame.draw.rect(screen, BUTTON_COLOR, up_button_rect)
    pygame.draw.rect(screen, BUTTON_COLOR, down_button_rect)
    pygame.draw.rect(screen, BUTTON_COLOR, left_button_rect)
    pygame.draw.rect(screen, BUTTON_COLOR, right_button_rect)

    # for fps
    pygame.display.flip()
    fps = pygame.time.Clock()
    fps.tick(120)


pygame.quit()
sys.exit()