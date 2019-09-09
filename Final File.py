import pygame

pygame.init() #initiates pygame

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

display_width = 1000
display_height = 750
gameDisplay = pygame.display.set_mode((display_width,display_height)) #sets resolution

pygame.display.set_caption('Tank 19 V0.2.0') #sets title

clock = pygame.time.Clock() #sets clock speed


tankImg = pygame.image.load('Images/Tank.jpg')
def tank(x,y):
    gameDisplay.blit(tankImg, (x,y)) #displays tank1 (gold) on the window

tankImg2 = pygame.image.load('Images/Tank2.jpg')
def tank2(x2,y2):
    gameDisplay.blit(tankImg2, (x2,y2)) #displays tank2 (silver) on the window

tank_width = 15
tank_height = 17 #defines width and height of both tanks

xBoundary = False
yBoundary = False
x2Boundary = False
y2Boundary = False #initiates the statement where a tank is on boundary or not

def main_game_loop():
    x = display_width * 0.5
    y = display_height * 0.8
    x2 = display_width * 0.5
    y2 = display_height * 0.2 #sets initial position for both tanks
    x_change = 0
    y_change = 0
    x2_change = 0
    y2_change = 0 #sets initial speed for both tanks

    gameExit = False #initiate game loop

    while not gameExit:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if xBoundary == False: #when tank1 isn't on left/right boundary
                    if event.key == pygame.K_LEFT:
                        x_change = -5
                    elif event.key == pygame.K_RIGHT:
                        x_change = 5 #sets horizontal velocity of tank1
                if yBoundary == False: #when tank1 isn't on up/down boundary
                    if event.key == pygame.K_UP:
                        y_change = -5
                    elif event.key == pygame.K_DOWN:
                        y_change = 5 #sets vertical velocity of tank1
                if x2Boundary == False: #when tank2 isn't on left/right boundary
                    if event.key == pygame.K_a:
                        x2_change = -5
                    elif event.key == pygame.K_d:
                        x2_change = 5 #sets horizontal velocity of tank2
                if y2Boundary == False: #when tank2 isn't on up/down boundary
                    if event.key == pygame.K_w:
                        y2_change = -5
                    elif event.key == pygame.K_s:
                        y2_change = 5 #sets vertical velocity of tank2
            if event.type == pygame.KEYUP:
                x_change = 0
                y_change = 0
                x2_change = 0
                y2_change = 0 #If no movement key is pressed, set all speeds to 0

        x = x + x_change
        y = y + y_change
        x2 = x2 + x2_change
        y2 = y2 + y2_change #executes all movements to be done based on velocities of both tanks

        gameDisplay.fill(white) #resets the window to white
        tank(x,y)
        tank2(x2,y2) #"draws" the two tanks at their new locations

        if x > (display_width - tank_width) or x < 0: #detects if tank1 is on left/right boundary
            xBoundary = True #if it is, set the statement to True to it can't move in the next tick
            if x < 0:
                x = 0
            else:
                x = display_width - tank_width #if tank1 is on left/right boundary set it back to place (on the boundary)
        else:
            xBoundary = False #if tank1 isn't on left/right boundary set the statement to False (so it can move in the next tick)
        if y > (display_height - tank_height) or y < 0: #detects if tank1 is on up/down boundary
            yBoundary = True #if it is, set the statement to True to it can't move in the next tick
            if y < 0:
                y = 0
            else:
                y = display_height - tank_height #if tank1 is on up/down boundary set it back to place (on the boundary)
        else:
            yBoundary = False #if tank1 isn't on up/down boundary set the statement to False (so it can move in the next tick)
        if x2 > (display_width - tank_width) or x2 < 0: #detects if tank2 is on left/right boundary
            x2Boundary = True #if it is, set the statement to True to it can't move in the next tick
            if x2 < 0:
                x2 = 0
            else:
                x2 = display_width - tank_width #if tank2 is on left/right boundary set it back to place (on the boundary)
        else:
            x2Boundary = False #if tank2 isn't on left/right boundary set the statement to False (so it can move in the next tick)
        if y2 > (display_height - tank_height) or y2 < 0: #detects if tank2 is on up/down boundary
            yBoundary = True #if it is, set the statement to True to it can't move in the next tick
            if y2 < 0:
                y2 = 0
            else:
                y2 = display_height - tank_height #if tank2 is on up/down boundary set it back to place (on the boundary)
        else:
            y2Boundary = False #if tank2 isn't on up/down boundary set the statement to False (so it can move in the next tick)
        
        pygame.display.update() #update the window
        clock.tick(30) #sets the frame rate for the window
        
main_game_loop()
pygame.quit()
quit()
