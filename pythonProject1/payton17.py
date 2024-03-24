import pygame
import sys

pygame.init()
play = True

class Player:
    def __init__(self, pos, screen, radius):
        self.pos = pos
        self.screen = screen
        self.radius = radius

    def display(self):
        pygame.draw.circle(self.screen, (255, 0, 0), self.pos, self.radius)

screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()  # Create a clock object to control the frame rate

while play:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False  # Exit the loop when the window is closed

    pos = pygame.mouse.get_pos()
    screen.fill((167, 235, 255))

    player = Player(pos, screen, 50)  # Create a player object with a radius of 50
    player.display()  # Display the player (circle)

    pygame.display.flip()  # Update the display

    clock.tick(120)  # Limit frame rate to 120 fps

pygame.quit()  # Quit pygame properly
sys.exit()  # Exit the program