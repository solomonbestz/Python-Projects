import pygame

from pygame.locals import *

SIZE = width, height = (600, 600) #Relative screen size
road_w = int(width/ 1.3)
road_strip = int(width/15)


# Function to draw a rectangle
def draw_rect(display, color, rectangle):
    pygame.draw.rect(
        display, #display
        color , #color
        rectangle #rectangle
    )

# FUnction to draw image 
def load_image(screen, file_path, img_size, rect_center):
    image = pygame.image.load(file_path)
    image = pygame.transform.scale(image, (img_size))

    image_location = image.get_rect()
    image_location.center = rect_center
    screen.blit(image, image_location)
    pygame.display.update()




pygame.init()
running = True
screen = pygame.display.set_mode(SIZE) #Initializing the screen 
pygame.display.set_caption("Bestz car game") #Game title 
screen.fill((90, 90, 90)) #Game background color

draw_rect(screen, (50, 50, 50), (width/2-road_w/2, 0, road_w, height)) # Rectangle for road
draw_rect(screen, (255,255,255), (width/2-road_strip/2, 0, road_strip, height /2.5)) #First strip
draw_rect(screen, (255,255,255), (width/2-road_strip/2, 400, road_strip, height/2.5)) #Second strip
draw_rect(screen, (255, 255, 0 ), (width/2 - road_w/2 + road_strip / 4, 0, road_strip/5, height)) #left Side strip
draw_rect(screen, (255, 255, 0 ), (width - road_w/5 + road_strip / 7, 0, road_strip/5, height)) #right Side strip


pygame.display.update() #Apply changes

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    load_image(screen, "py_game/player_car.png", (150, 150), (width/2 - road_w/4, height * 0.88) )
    
pygame.quit()