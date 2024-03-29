import pygame as space
from pygame.locals import *
import random, math


# Initialise the space
space.init()

# Creating the screen instance
screen_width = 800
screen_height = 600
screen = space.display.set_mode((screen_width, screen_height))

"""
Here we declared global variables of objects coordinate 
"""
# Player coordinate assigned to player_x and player_y variable
player_x, player_y = 370, 480

# Bullet coordinate assigned to bullet_x and bullet_y variable
bullet_x, bullet_y = 0, 480

# Muzzle flash coordinate assigned to muzzle_x and muzzle_y variable
muzzle_x, muzzle_y = 0, 480

# Global Score Variable
score_value = 0

"""
Bullet state

Ready - You can't see the bullet on the screen
Fire - The bullet is currently moving

"""
bullet_state = "ready"

"""
Here we declared global variables and lists to change object's position
"""

# List for enemy player
enemy_img = []

# Enemy coordinate assigned to enemy_x and enemy_y list
enemy_x, enemy_y = [], []
# Change position of enemy's x and y coordinate
change_enemy_x, change_enemy_y = [], []
# Change position of player's x and y coordinate
change_player_x, change_player_y = 0, 0

# Change position of bullet's x and y coordinate
change_bullet_x, change_bullet_y = 0, 3

# Number of enemies
num_of_enemy = 0

"""
Here we are creating all the functions needed to run the game
"""
# Function to load image
def load_image(image_path):
    return space.image.load(image_path)


# Player Appear On Screen Function
def player(x, y):
    # Screen blit to display player on screen
    screen.blit(player_img, (x, y))


# Enemy Appear On Screen Function
def enemy(enemy_img, x, y):
    # Screen blit to display enemy on screen
    screen.blit(enemy_img, (x, y))


# Function to create multiple enemies
def multiple_enemies():
    global num_of_enemy, enemy_img, enemy_x, enemy_y, change_enemy_y, change_enemy_x
    x_range = range(1, 735, 100)
    y_range = range(1, 50, 10)

    num_of_enemy = 5
    enemy_x = random.sample(x_range, num_of_enemy)
    enemy_y = random.sample(y_range, num_of_enemy)

    for enem in range(num_of_enemy):
        enemy_img.append(load_image("Space_invader/space-invader.png"))
        change_enemy_x.append(0.7)
        change_enemy_y.append(0)


# Player Movement function for pressed event
def player_mov_pressed(event):
    global change_player_x, change_player_y
    if event.type == KEYDOWN:
        if event.key in [K_d, K_RIGHT]:
            change_player_x = 1
        if event.key in [K_a, K_LEFT]:
            change_player_x = -1
        if event.key in [K_w, K_UP]:
            change_player_y = -1
        if event.key in [K_s, K_DOWN]:
            change_player_y = 1


# Stops player's movement
def player_mov_released(event):
    global change_player_x, change_player_y
    if event.type == KEYUP:
        if event.key in [K_d, K_RIGHT] or event.key in [K_a, K_LEFT]:
            change_player_x = 0
        if event.key in [K_d, K_UP] or event.key in [K_a, K_DOWN]:
            change_player_y = 0


# Function to move enemy on x coordinate
def enemy_mov_x():
    global enemy_x

    for i in range(num_of_enemy):
        enemy_x[i] += change_enemy_x[i]


# Check enemy boundary
def check_enemy_boundary():
    global change_enemy_x, change_enemy_y, enemy_y

    for i in range(num_of_enemy):
        if enemy_x[i] > 735:
            change_enemy_y[i] += 20
            enemy_y[i] += change_enemy_y[i]
            change_enemy_x[i] = -0.9

        if enemy_x[i] < 1:
            change_enemy_y[i] += 20
            enemy_y[i] += change_enemy_y[i]
            change_enemy_x[i] = 0.9


# Check player boundary
def check_boundary():
    global player_x
    if player_x < 1:
        player_x = 1
    if player_x > 735:
        player_x = 735


# Display Player bullet
def bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bullet_img, (x + 16, y - 10))


# Display Bullet when space button pressed
def display_bullet(event):
    global bullet_state, bullet_x, bullet_y
    if event.type == KEYDOWN:
        if event.key in [K_SPACE]:
            if bullet_state == "ready":
                bullet_x = player_x
                bullet_y = player_y
                bullet(bullet_x, bullet_y)
                shoot_laser()


# Fire Bullet
def fire_bullet():
    global bullet_state, bullet_y
    if bullet_state is "fire":
        bullet(bullet_x, bullet_y)
        bullet_y -= change_bullet_y
    if bullet_y < 1:
        bullet_state = "ready"
        bullet_y = 480


# Collision Detection
def collision(point_b_x, point_b_y, point_a_x, point_a_y):
    distance = math.sqrt(
        (math.pow(point_b_x - point_a_x, 2) + math.pow(point_b_y - point_a_y, 2))
    )
    return distance


# Enemy Removal function after collision with bullet
def remove_enemy():
    global enemy_x, enemy_y, change_enemy_y, bullet_x, bullet_y, bullet_state, score_value

    for i in range(num_of_enemy):

        # Calling the collision function
        is_collide = collision(enemy_x[i], enemy_y[i], bullet_x, bullet_y)

        if is_collide < 27:
            # Reset Enemy's position
            enemy_explosion_sound() # Function call for enemy to explode
            enemy_x[i], enemy_y[i] = random.randint(1, 735), random.randint(1, 50)
            change_enemy_y[i] = 0

            # Reset Bullet
            bullet_state = "ready"
            bullet_x, bullet_y = 0, 480
            score_value += 1
            # print(f"Killed \n {score_value}")
    
def game_over():
    global running, enemy_x, enemy_y, change_enemy_y, player_x, player_y, score_value

    for i in range(num_of_enemy):
        # Checking enemy and player collision

        player_collision = collision(player_x, player_y, enemy_x[i], enemy_y[i])
    
        if player_collision < 45:
            print("We collided")
            running = False


# Display kill score
def display_score():
    text_x, text_y = 10, 10
    font = space.font.Font("Space_invader/prohuman.ttf", 32)
    score = font.render(f"Score: {score_value}", True, (255, 255, 255))
    screen.blit(score, (text_x, text_y))


# Sounds function
def sounds(path, **optional):
    sound_user = space.mixer.Sound(path)
    sound_user.set_volume(optional.get("volume"))
    sound_user.play(optional.get("loop"))


# Sound Function for background music
def background_sound():
    sounds("Space_invader/background-music.wav", volume=0.3, loop=-1)


# Sound Function to shoot laser
def shoot_laser():
    sounds("Space_invader/laser-gun.mp3", volume=0.5, loop=0)

# Sound Function for enemy explosion
def enemy_explosion_sound():
    sounds("Space_invader/enemy-explosion.wav", volume=1, loop=0)


"""
Here we are loading all images to their respective variables
"""
# Game title
space.display.set_caption("Space Invader")
# Load Game Icon and assign to the icon variable
icon = load_image("Space_invader/spaceship_32.png")
space.display.set_icon(icon)
# Load Background Image and assign to the backgroud variable
background = load_image("Space_invader/Background.jpg")
# Load Player Image and assign to the player_img variable
player_img = load_image("Space_invader/player.png")
# Load Bullet Image and assign to the bullet_img variable
bullet_img = load_image("Space_invader/bullet.png")


# Calling the multiple enemy function
multiple_enemies()

# Calling background music
background_sound()

"""
Here is the game loop
"""

# Game Loop
running = True
while running:
    # RGB color to change screen background color
    # screen.fill((12.16, 25.88, 46.67))  # (12, 25, 46)
    # Add background image
    screen.blit(background, (0, 0))

    # Call the display score function
    display_score()

    # Enemy Movement
    enemy_mov_x()

    # Event loop handler
    for event in space.event.get():
        if event.type == QUIT:
            running = False
        player_mov_pressed(event)
        player_mov_released(event)
        display_bullet(event)

    # Check if enemy has reached edge and push down
    check_enemy_boundary()
    # Check if player has reached edge
    check_boundary()
    # Calling the function to remove enemy
    remove_enemy()

    # Calling the function to check game over
    game_over()
    # Bullet Movement
    fire_bullet()
    # Player movement
    player_x += change_player_x
    player_y += change_player_y

    # Display Player on screen
    player(player_x, player_y)

    for enem in range(num_of_enemy):
        enemy(enemy_img[enem], enemy_x[enem], enemy_y[enem])

    space.display.update()
