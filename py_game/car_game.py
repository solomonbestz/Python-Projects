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

pygame.quit()