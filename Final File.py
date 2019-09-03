import pygame

pygame.init() #initiates pygame

gameDisplay = pygame.display.set_mode((1440,1080)) #sets resolution

pygame.display.set_caption("Tank 19 V0.1.1") #sets title

clock = pygame.time.Clock() #sets clock speed

done = False #initiate game loop

while not done:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done= True

        print(event)

    pygame.display.update()
    clock.tick(30)

pygame.quit()
quit()
