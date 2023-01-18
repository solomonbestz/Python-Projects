import pygame as space
from pygame.locals import *


# Initialise the space 
space.init()

# Creating the screen instance
screen = space.display.set_mode((800, 600))

# Player coordinate assigned as tuple to player_cord
player_x, player_y = 370, 480

# Function to load image
def load_image(image_path):
    return space.image.load(image_path)

# Player function
def player():
    # Screen blit to display player in screen
    screen.blit(player_img, (player_x, player_y))

# Player Movement function
def player_mov(event):
    global player_x
    if event.type == KEYDOWN:
        if event.key in [K_d, K_RIGHT]:
            print("Pressed Right")
            player_x += 5
        if event.key in [K_a, K_LEFT]:
            print("Pressed Left")
            player_x -= 5
    

# Game title and logo
space.display.set_caption("Space Invader")
icon = load_image('Space_invader/spaceship_32.png')
space.display.set_icon(icon)

# Loaded Player Image assigned to the player_img variable
player_img = load_image('Space_invader/player.png')


# Game Loop
running = True
while running:
    # RGB color to change screen background color 
    screen.fill((12.16, 25.88, 46.67)) #(12, 25, 46)
    for event in space.event.get():
        if event.type == QUIT:
            running = False 
        player_mov(event)
    player()
    space.display.update()


