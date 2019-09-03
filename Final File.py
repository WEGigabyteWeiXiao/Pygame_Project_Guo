import pygame

pygame.init() #initiates pygame

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

display_width = 800
display_height = 600
gameDisplay = pygame.display.set_mode((display_width,display_height)) #sets resolution

pygame.display.set_caption('Tank 19 V0.1.2') #sets title

clock = pygame.time.Clock() #sets clock speed


tankImg = pygame.image.load('D:/Schools/3 Dulwich College/3 Computer Science/Pygame Project/Images/Tank.jpg')
def tank(x,y):
    gameDisplay.blit(tankImg, (x,y))
x = display_width * 0.5
y = display_height * 0.8
x_change = 0
y_change = 0

done = False #initiate game loop

while not done:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done= True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = -5
            elif event.key == pygame.K_RIGHT:
                x_change = 5
            elif event.key == pygame.K_UP:
                y_change = -5
            elif event.key == pygame.K_DOWN:
                y_change = 5

        if event.type == pygame.KEYUP:
            x_change = 0
            y_change = 0

    x = x + x_change
    y = y + y_change

    gameDisplay.fill(white)
    tank(x,y)
    pygame.display.update()
    clock.tick(30)

pygame.quit()
quit()
