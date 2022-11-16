import pygame
from pygame.locals import *
import random

SIZE = width, height = (600, 600) #Relative screen size
road_w = int(width/ 1.3) # Road width
road_strip = int(width/15) # Road strip width
ENEMY_SPEED = 1

RIGHT_LANE = width/2 + road_w/4
LEFT_LANE = width/2 - road_w/4




# Function to draw a rectangle
def draw_rect(display, color, rectangle):
    pygame.draw.rect(
        display, #display
        color , #color
        rectangle #rectangle
    )

# Function to draw image 
def load_image(file_path, img_size, rect_center):
    image = pygame.image.load(file_path)
    image = pygame.transform.scale(image, (img_size))

    image_location = image.get_rect()
    image_location.center = rect_center
    
    return [image, image_location]


#Display shape functio
def display_road():
    draw_rect(screen, (50, 50, 50), (width/2-road_w/2, 0, road_w, height)) # Rectangle for road
    draw_rect(screen, (255,255,255), (width/2-road_strip/2, 0, road_strip, height)) #Middle way trip
    draw_rect(screen, (255, 255, 0 ), (width/2 - road_w/2 + road_strip / 4, 0, road_strip/5, height)) #left Side strip
    draw_rect(screen, (255, 255, 0 ), (width - road_w/5 + road_strip / 7, 0, road_strip/5, height)) #right Side strip

# Enemy movement function
def enemy_movement(enemy_loc):
    # Animate enemy vehicle
    enemy_loc[1] += ENEMY_SPEED
    if enemy_loc[1] > height:
        enemy_loc[1] = -200
        if random.randint(0, 1) == 0:
            enemy_loc.center = RIGHT_LANE -1, -200 
            sound1[0].play()
        else:
            enemy_loc.center = LEFT_LANE, -200

def end_game(player_loc, enemy_loc):
    if player_loc[0] ==  enemy_loc[0] -25 and enemy_loc[1] > player_loc[1] - 100:
        print("Game Over!!")
        exit()

def level_up(counter):
    global ENEMY_SPEED
    if counter == 5000:
        ENEMY_SPEED += 0.15
        counter = 0
        print("Level Up", ENEMY_SPEED)
    return counter

def sounds():
    car_sound1 = pygame.mixer.Sound("py_game/car_sound.mp3")
    return [car_sound1]


    

pygame.init()
pygame.mixer.init()


running = True
screen = pygame.display.set_mode(SIZE) #Initializing the screen 
pygame.display.set_caption("Bestz Race") #Game title 
screen.fill((90, 90, 90)) #Game background color





player = load_image("py_game/player_car.png", (150, 150), (LEFT_LANE, height * 0.88))
enemy = load_image("py_game/enemy_car.png", (100, 130), (RIGHT_LANE - 1, height * 0.1))


counter = 0
sound1 = sounds()

while running:
    counter += 1
    enemy_movement(enemy[1])
    count = level_up(counter)
    counter = count
    end_game(player[1], enemy[1])
    # EVent Listener
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if event.type == KEYDOWN:
            if event.key in [K_d, K_RIGHT]:
                player[1] = player[1].move([int(road_w/2), 0])
                
            if event.key in [K_a, K_LEFT]:
                player[1] = player[1].move([int(-road_w/2), 0])
                
    display_road()
    

    screen.blit(player[0], player[1])
    screen.blit(enemy[0], enemy[1])  
    pygame.display.update() #Apply Changes


    
pygame.quit()