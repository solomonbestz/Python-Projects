import pygame

# Initialise the pygame 
pygame.init()

# Creating the screen instance
screen = pygame.display.set_mode((800, 600))

# Game title and logo
pygame.display.set_caption("Space Invader")
icon = pygame.image.load('Space_invader/spaceship_32.png')
pygame.display.set_icon(icon)

# Game Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 
    
    # RGB color to change screen background color 
    screen.fill((12.16, 25.88, 46.67)) #(12, 25, 46)
    pygame.display.update()
