import pygame

pygame.init()

display_width = 800
display_height = 700
gameDisplay = pygame.display.set_mode([display_width,display_height])
#Sets resolution of the game window and actually creates it

pygame.display.set_caption('Tank 19 V0.6 (07-OCT-19)')
#Sets title of the game window

clock = pygame.time.Clock()
#Sets the clock speed of the game

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
brown = (110,64,64)
yellow = (255,255,0)
#Sets up RGB values of all the colours

class Wall(pygame.sprite.Sprite):
#Constructor function for walls
    def __init__(self,x,y,width,height,color):
        pygame.sprite.Sprite.__init__(self)
        #calls the parent class (sprite) constructor

        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        #creates an image of the wall, and fill it with color sat.

        self.rect = self.image.get_rect() 
        self.rect.y = y
        self.rect.x = x
        #Make the top-left corner of the "tank" the passed-in location


class Player(pygame.sprite.Sprite):

    change_x = 0
    change_y = 0
    #initiates player's speed and hitpoint
    
    def __init__(self,x,y,colour,hp):
    #constructor
        pygame.sprite.Sprite.__init__(self)
        #Call the parent's constructor

        self.image = pygame.Surface([15,15]) 
        self.image.fill(colour)
        #Sets height, width and colour of the tank

        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
        #Make the top-left corner of the "tank" the passed-in location

        self.hp = hp
        #Initialises the hp of the player

    def changespeed(self,x,y):
        self.change_x += x
        self.change_y += y
        #Changes the speed of the player when related keys are pressed

    def move(self, walls):
    #Decides the position of the tank in the next tick
        self.rect.x += self.change_x
        #Moves along horizontal direction

        block_hit_list = pygame.sprite.spritecollide(self,walls,False)
        #Check if the tank is going to hit the wall in the horizontal in the next tick
        for block in block_hit_list:
        #If it is hitting in the horizontal direction
            if self.change_x > 0:
            #If the tank is going to the right
                self.rect.right = block.rect.left
            else:
            #If the tank is going to the left
                self.rect.left = block.rect.right

        self.rect.y += self.change_y
        #moves along vertical direction

        block_hit_list = pygame.sprite.spritecollide(self,walls,False)
        #Check if the tank is going to hit the wall in the vertical in the next tick
        for block in block_hit_list:
        #If it is hitting in the vertical direction
            if self.change_y > 0:
            #if the tank is going to the bottom
                self.rect.bottom = block.rect.top
            else:
            #If the tank is going to the top
                self.rect.top = block.rect.bottom

    def hp_change(self, hpchange):
    #Changes the hp of the player in case of a hit or something else
        self.hp = self.hp + hpchange
        #Actually changes the hp of the player
        hpchange = 0
        #Reset the value so the value will not be changed constantly

    def get_hp(self):
    #Getter method for hp (in order to display on the scoreboard)
        return self.hp
        

class Map():
#Base class for all maps

    wall_list = None
    enemy_sprites = None
    #Initialises wall list and stuffs

    def __init__(self):
    #Constructor
        self.wall_list = pygame.sprite.Group()
        self.enemy_sprites = pygame.sprite.Group()
        #Makes both wall_list and enemy_sprites groups


class M_Classic(Map):
#Class for map M_Classic
    def __init__(self):
        Map.__init__(self)
        #Calls the constructor of its parent class

        walls = [ [0,0,10,600,brown], #Left boundary
                  [0,0,800,10,brown], #Top boundary
                  [790,0,10,600,brown], #Right boundary
                  [0,590,800,20,brown], #Bottom boundary
                  [50,290,330,20,brown], #Mid Wall (Left)
                  [420,290,330,20,brown], #Mid Wall (Right)
                  [50,50,20,500,brown], #Left road Wall
                  [730,50,20,500,brown], #Right road Wall
                  [360,200,20,200,brown], #Mid road Wall (Left)
                  [420,200,20,200,brown], #Mid road Wall (Right)
                  [670,350,20,250,brown], #BR corner walkway Wall
                  [670,0,20,250,brown], #TR corner Walkway Wall
                  [110,350,20,250,brown], #BL corner walkway Wall
                  [110,0,20,250,brown], #TL corner walkway Wall
                  [200,45,400,20,brown], #Top Wall 1
                  [200,100,400,20,brown], #Top Wall 2
                  [200,480,400,20,brown], #Bottom Wall 1
                  [200,535,400,20,brown] #Bottom Wall 2
                ]
        #This is the list of walls in map "M_Classic"

        for item in walls:
            wall = Wall(item[0],item[1],item[2],item[3],item[4])
            self.wall_list.add(wall)
        #Actually adds all the walls
            

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()
#Function for setting massage display


def start_menu():
    intro = True
    #Sets the initial value of iteration condition

    while intro == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                #If the window is closed, actually close it
                
            if event.type == pygame.KEYDOWN:
            #Detects if the user pressed a button
                if event.key == pygame.K_c:
                    intro = False
                #If [C] is pressed let the game enter the main loop
                    
                if event.key == pygame.K_v:
                    pygame.quit()
                    quit()
                #If [V] is pressed quit the game

        gameDisplay.fill(white)
        #fill the screen with white
        
        canteur115 = pygame.font.Font("Fonts/CENTAUR.TTF", 115)
        canteur25 = pygame.font.Font("Fonts/CENTAUR.TTF", 25)
        #Initialise fonts used in the subroutine
        
        TextSurf, TextRect = text_objects("Tank 19", canteur115)
        TextRect.center = (400,250)
        #Displays title of game
        
        TextSurf2, TextRect2 = text_objects("Game Version: V0.6 Updated 07-Oct-19", canteur25)
        TextRect2.center = (400,300)
        #Displays version number of game
        
        TextSurf3, TextRect3 = text_objects("Press [C] to start the game", canteur25)
        TextRect3.center = (227,500)
        TextSurf4, TextRect4 = text_objects("Press [V] to quit the game (or simply press the 'X' in the corner)",canteur25)
        TextRect4.center = (400,530)
        #Displays instructions on the window
        
        gameDisplay.blit(TextSurf, TextRect)
        gameDisplay.blit(TextSurf2, TextRect2)
        gameDisplay.blit(TextSurf3, TextRect3)
        gameDisplay.blit(TextSurf4, TextRect4)
        pygame.display.update()
        #Makes all changes made above to take effect
        

def main():
#Main program

    player1 = Player(392,20,green,100)
    movingsprites = pygame.sprite.Group()
    movingsprites.add(player1)
    #Creates the player (and the AI), adds them into the sprite list

    maps = []
    #Creates a list of maps, so it will possible to play multiple maps in a single game

    gamemap = M_Classic()
    maps.append(gamemap)
    #Puts map "M_Classic" into the map list

    current_map_id = 0
    current_map = maps[current_map_id]
    #Makes the "current map" in use

    clock = pygame.time.Clock()
    #Sets the clock speed of the game

    GameExit = False
    
    while not GameExit:
    #Event processing starts here
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                GameExit = True
            #Quit the game if the user chose to do so.

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    player1.changespeed(-6,0)
                if event.key == pygame.K_d:
                    player1.changespeed(6,0)
                if event.key == pygame.K_w:
                    player1.changespeed(0,-6)
                if event.key == pygame.K_s:
                    player1.changespeed(0,6)
                #When a direction key is pressed let the player to do according movements

                if event.key == pygame.K_m:
                    start_menu()
                #When M is pressed go back to main game menu

                if event.key == pygame.K_v:
                    pygame.quit()
                    quit()
                #When V is pressed quit the game

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    player1.changespeed(6,0)
                if event.key == pygame.K_d:
                    player1.changespeed(-6,0)
                if event.key == pygame.K_w:
                    player1.changespeed(0,6)
                if event.key == pygame.K_s:
                    player1.changespeed(0,-6)
                #When a direction key is released reset the player's speed

        #Event processing ends here

        #Additional drawing starts here

        gameDisplay.fill(white)
        #Fills the entire window with white to initialise

        movingsprites.draw(gameDisplay)
        current_map.wall_list.draw(gameDisplay)
        #Draws all sprites and walls

        canteur20 = pygame.font.Font("Fonts/CENTAUR.TTF", 20)
        #Defines fonts used in main game loop

        TextSurf5, TextRect5 = text_objects("Press [M] to go to game menu    Press [V] to quit the game", canteur20)
        TextRect5.center = (220,680)
        gameDisplay.blit(TextSurf5, TextRect5)
        #Displays text for going back to main menu or quit the game

        TextSurf6, TextRect6 = text_objects("Player1 HP:" + str(player1.get_hp()), canteur20)
        TextRect6.center = (65,625)
        gameDisplay.blit(TextSurf6, TextRect6)
        #Displays information of the hp remaining hp of the player

        #Additional drawing stops here

        player1.move(current_map.wall_list)
        #Updates the position of player in each tick
        
        pygame.display.update()
        #Updates the game window
        
        clock.tick(30)
        #Sets game frame rate to 30

    pygame.quit()
    #Quit the game when the game is no longer inside the main loop

if __name__ == "__main__":
    start_menu()
    main()
#Calls main menu at the start of the game
