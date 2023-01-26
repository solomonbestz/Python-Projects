import pygame

pygame.init()

gameDisplay = pygame.display.set_mode((800,600))
clock = pygame.time.Clock()

crashed = False

counter = 1
while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
    
    pygame.display.update()
    print(counter)
    counter += 1
    clock.tick(1) # will be 10 in the next run 