import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the screen
SCREEN_WIDTH = int(1080 * 1)  # Make the screen 40% smaller
SCREEN_HEIGHT = int(2400 * 1)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Zyron")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
DARK_GRAY = (100, 100, 100)
LIGHT_GRAY = (150, 150, 150)
BEIGE = (228, 216, 180)

# Player
player_bg_color = BEIGE
player_bg_width = SCREEN_WIDTH // 1.08  # Adjusted size of the player's background
player_bg_height = SCREEN_HEIGHT // 1.5
player_bg_rect = pygame.Rect((SCREEN_WIDTH // 2 - player_bg_width // 2, SCREEN_HEIGHT // 30),
                             (player_bg_width, player_bg_height))  # Adjusted position

# Load player image
# Define a variable for player size
player_size = min(SCREEN_WIDTH, SCREEN_HEIGHT) // 3  # Adjusted for smaller screen

# Load player image and scale it to the player size
player_image = pygame.image.load('player_image.png')  # Replace 'player_image.png' with your image file path
player_image = pygame.transform.scale(player_image, (player_size, player_size))  # Scale the player image

# Create a player rectangle based on the player image size
player_rect = player_image.get_rect(center=player_bg_rect.center)

# Button dimensions and positions
BUTTON_SIZE = int(SCREEN_WIDTH / 5)  # Adjusted button size, increased from previous
BUTTON_MARGIN = 15
BUTTON_SPACING = BUTTON_SIZE + BUTTON_MARGIN
BUTTON_START_X = SCREEN_WIDTH // 2 - BUTTON_SIZE // 2  # Center the buttons horizontally
BUTTON_START_Y = SCREEN_HEIGHT * 15 // 20  # 2/3 lower of the screen  # Center the buttons vertically

# Button colors
BUTTON_COLOR = DARK_GRAY
BUTTON_ACTIVE_COLOR = LIGHT_GRAY
BUTTON_HOVER_COLOR = (200, 200, 0)  # Yellow for hover effect
BUTTON_PRESS_COLOR = (0, 200, 200)  # Cyan for pressed effect

# Define colors for each button
# UP_BUTTON_COLOR = (255, 0, 0)  # Red
# DOWN_BUTTON_COLOR = (0, 255, 0)  # Green
# LEFT_BUTTON_COLOR = (0, 0, 255)  # Blue
# RIGHT_BUTTON_COLOR = (255, 255, 0)  # Yellow

BUTTON_COLOR2 = (39, 35, 36)

# Movement distance based on screen size
movement_distance = min(SCREEN_WIDTH, SCREEN_HEIGHT) // 9  # Adjusted for smaller screen

# Buttons
up_button_rect = pygame.Rect(BUTTON_START_X, BUTTON_START_Y, BUTTON_SIZE, BUTTON_SIZE)
down_button_rect = pygame.Rect(BUTTON_START_X, BUTTON_START_Y + BUTTON_SPACING, BUTTON_SIZE, BUTTON_SIZE)
left_button_rect = pygame.Rect(BUTTON_START_X - BUTTON_SPACING, BUTTON_START_Y + BUTTON_SPACING, BUTTON_SIZE,
                               BUTTON_SIZE)
right_button_rect = pygame.Rect(BUTTON_START_X + BUTTON_SPACING, BUTTON_START_Y + BUTTON_SPACING, BUTTON_SIZE,
                                BUTTON_SIZE)

# Define gravity constant
GRAVITY = 0.5  # Adjust as needed
# Create Clock object
clock = pygame.time.Clock()

# Vertical velocity of the player (initially set to 0)
player_vertical_velocity = 0
# Jump velocity
JUMP_VELOCITY = -10  # Adjust as needed

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
                    player_vertical_velocity = JUMP_VELOCITY  # Set vertical velocity to jump velocity
                elif down_button_rect.collidepoint(event.pos):
                    player_rect.y += movement_distance
                elif left_button_rect.collidepoint(event.pos):
                    player_rect.x -= movement_distance
                elif right_button_rect.collidepoint(event.pos):
                    player_rect.x += movement_distance
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player_vertical_velocity = JUMP_VELOCITY  # Set vertical velocity to jump velocity
            elif event.key == pygame.K_DOWN:
                player_rect.y += movement_distance
            elif event.key == pygame.K_LEFT:
                player_rect.x -= movement_distance
            elif event.key == pygame.K_RIGHT:
                player_rect.x += movement_distance

    # Apply gravity to the player's vertical velocity
    player_vertical_velocity += GRAVITY

    # Update player's vertical position based on velocity
    player_rect.y += player_vertical_velocity

    # Keep player within screen bounds
    player_rect.x = max(player_bg_rect.left, min(player_rect.x, player_bg_rect.right - player_rect.width))
    player_rect.y = max(player_bg_rect.top, min(player_rect.y, player_bg_rect.bottom - player_rect.height))

    # Clear screen
    screen.fill(BUTTON_COLOR2)

    # Draw player background
    #pygame.draw.rect(screen, player_bg_color, player_bg_rect)
# Draw player background with rounded corners
    pygame.draw.rect(screen, player_bg_color, player_bg_rect, border_radius=20)
  # Adjust border_radius as needed

    # Draw player image
    screen.blit(player_image, player_rect)

    # Draw buttons with respective colors
    up_button_color = WHITE if up_button_rect.collidepoint(pygame.mouse.get_pos()) else BUTTON_COLOR
    down_button_color = WHITE if down_button_rect.collidepoint(pygame.mouse.get_pos()) else BUTTON_COLOR
    left_button_color = WHITE if left_button_rect.collidepoint(pygame.mouse.get_pos()) else BUTTON_COLOR
    right_button_color = WHITE if right_button_rect.collidepoint(pygame.mouse.get_pos()) else BUTTON_COLOR

    pygame.draw.rect(screen, up_button_color, up_button_rect)
    pygame.draw.rect(screen, down_button_color, down_button_rect)
    pygame.draw.rect(screen, left_button_color, left_button_rect)
    pygame.draw.rect(screen, right_button_color, right_button_rect)

    # for fps
    pygame.display.flip()
    clock.tick(120)

pygame.quit()
sys.exit()
