import pygame

pygame.init()

display_width = 800
display_height = 700
gameDisplay = pygame.display.set_mode([display_width,display_height])
#Sets resolution of the game window and actually creates it

pygame.display.set_caption('Tank 19 V1.1 (08-NOV-19)')
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
dyellow = (150,150,0)
#Sets up RGB values of all the colours

bullet_list = pygame.sprite.Group()
#Creates a list for bullets


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
    #initialises player's speed and hitpoint

    hp = 500
    max_hp = 500
    mp = 2000
    #Initialises player's hp and mp

    recoveryCount = 4
    #Initialises player's hp recovery counter
    
    def __init__(self,x,y,colour):
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

    def changespeed(self,x,y):
        self.change_x += x
        self.change_y += y
        #Changes the speed of the player when related keys are pressed

    def move(self, walls):
    #Decides the position of the tank in the next tick
        self.rect.x += self.change_x
        #Moves walong horizontal direction

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

        block_hit_list = pygame.sprite.spritecollide(self,bullet_list,True)
        #Check if the player is being hit by a a bullet
        for block in block_hit_list:
        #If a bullet did hit a player
            self.hp = self.hp - 50
        
    def shoot(self):
        bullet_x = self.rect.x
        bullet_y = self.rect.y
        bullet = Bullet(bullet_x + self.change_x + 5, bullet_y + self.change_y + 5)
        #Creates a bullet when the player presses space
        bullet.speed_x = self.change_x * 3
        bullet.speed_y = self.change_y * 3
        #Set the initial position of the bullet
        bullet_list.add(bullet)
        self.mp = self.mp - 60
        #Adds the bullet into the game and deducts mp required from the player

    def get_change_x(self):
    #Getter method for horizontal speed
        return self.change_x

    def get_change_y(self):
    #Getter method for vertical speed
        return self.change_y

    def get_pos_x(self):
    #Getter method for horizontal position
        return self.rect.x

    def get_pos_y(self):
    #Getter method for vertical position
        return self.rect.y

    def hp_change(self, hpchange):
    #Changes the hp of the player in case of a hit or something else
        self.hp = self.hp + hpchange
        #Actually changes the hp of the player
        hpchange = 0
        #Reset the value so the value will not be changed constantly

    def mp_update(self):
    #Changes the mp of the player in case of a shoot and natural recovery
        if self.mp < 1000:
            self.mp = self.mp + 1
            if self.mp < 400:
                self.mp = self.mp + 1
                if self.mp < 160:
                    self.mp = self.mp + 1
        #If mp os less than 1000/400/160, recover mp at regular/double/triple speed
        if self.mp > 1000:
            self.mp = self.mp - 1
        #If mp is higher than maximum, slowly deduct it

    def hp_recovery(self):
        if self.recoveryCount > 0:
            self.recoveryCount = self.recoveryCount - 1
        #When it isn't the tick for recovery yet, decrease the counter
        else:
        #When it is the tick for hp recovery
            self.recoveryCount = 6
            #Resets the counter
            if self.hp < self.max_hp * 0.15:
                self.hp = self.hp + 2
            elif self.hp < self.max_hp:
                self.hp = self.hp + 1
            #Recover hp, if lower than 15% of max hp, double the speed
        if self.mp >= 1000:
            self.recoveryCount = self.recoveryCount - 1
        #If the player is at full mp, double the speed of recovery
                        

    def get_hp(self):
    #Getter method for hp (in order to display on the scoreboard)
        return self.hp

    def get_mp(self):
    #Getter method for mp
        return self.mp

    def get_max_hp(self):
    #Getter method for max_hp
        return self.max_hp

    def set_pos(self,newx,newy):
    #Subroutine for setting position of player
        self.x = newx
        self.y = newy


class Bullet(pygame.sprite.Sprite):
#Base class for bullets in the game
    
    def __init__(self, x, y):
    #Constructor for the class
        pygame.sprite.Sprite.__init__(self)
        #Calls the constructor of its parent class

        self.image = pygame.Surface([5,5])
        self.image.fill(black)
        #Creates a bullet with size 5,5 and fill it with black

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        #Sets the bullet as a rectangle

        self.speed_x = 0
        self.speed_y = 0
        #Sets speed of bullets

    def move(self):
        self.rect.x += self.speed_x
        #Moves bullets along horizontal direction
        
        self.rect.y += self.speed_y
        #Moves bullets along vertical direction


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
                if event.key == pygame.K_1:
                    intro = False
                #If [1] is pressed let the game enter tutorial
                    
                if event.key == pygame.K_2:
                    pygame.quit()
                    quit()
                #If [2] is pressed quit the game

                if event.key == pygame.K_3:
                    tutorial()
                #If [3] is pressed go to tutorial

        gameDisplay.fill(white)
        #fill the screen with white
        
        canteur115 = pygame.font.Font("Fonts/CENTAUR.TTF", 115)
        canteur25 = pygame.font.Font("Fonts/CENTAUR.TTF", 25)
        #Initialise fonts used in the subroutine
        
        TextSurf, TextRect = text_objects("Tank 19", canteur115)
        TextRect.center = (400,250)
        #Displays title of game
        
        TextSurf2, TextRect2 = text_objects("Game Version: V1.1 Updated 08-Nov-19", canteur25)
        TextRect2.center = (400,300)
        #Displays version number of game
        
        TextSurf3, TextRect3 = text_objects("Press [1] to start the game", canteur25)
        TextRect3.center = (227,500)
        TextSurf4, TextRect4 = text_objects("Press [2] to quit the game (or simply press the 'X' in the corner)",canteur25)
        TextRect4.center = (400,530)
        TextSurf201, TextRect201 = text_objects("Press [3] for tutorial", canteur25)
        TextRect201.center = (200,560)
        #Displays instructions on the window
        
        gameDisplay.blit(TextSurf, TextRect)
        gameDisplay.blit(TextSurf2, TextRect2)
        gameDisplay.blit(TextSurf3, TextRect3)
        gameDisplay.blit(TextSurf4, TextRect4)
        gameDisplay.blit(TextSurf201, TextRect201)
        pygame.display.update()
        #Makes all changes made above to take effect


def tutorial():
    tutorial = True
    
    while tutorial == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            #If the window is closed, close it
            if event.type == pygame.KEYDOWN:
            #Detects if the user pressed a button
                if event.key == pygame.K_1:
                    tutorial = False
                if event.key == pygame.K_2:
                    start_menu()
                if event.key == pygame.K_3:
                    pygame.quit()
                    quit()
        gameDisplay.fill(white)
        
        canteur60 = pygame.font.Font("Fonts/CENTAUR.TTF", 60)
        canteur25 = pygame.font.Font("Fonts/CENTAUR.TTF", 25)
        #Define all fonts used in this subroutine

        TextSurf100, TextRect100 = text_objects("Tank 19 Tutorial", canteur60)
        TextRect100.center = (400,150)
        #Displays title

        TextSurf101, TextRect101 = text_objects("Movement keys: P1:[W][A][S][D]; P2:[I][J][K][L].", canteur25)
        TextRect101.center = (400,300)
        TextSurf102, TextRect102 = text_objects("Shooting keys: P1:[C]; P2:[N]. Each player start with 500 maximum HP", canteur25)
        TextRect102.center = (400,350)
        TextSurf103, TextRect103 = text_objects("and 2000 MP. Each player has a maximum MP of 1000. Your MP will recover",canteur25)
        TextRect103.center = (400,375)
        TextSurf104, TextRect104 = text_objects("at a rate of 30 per second. However, when it is lower than 400/160, the rate", canteur25)
        TextRect104.center = (400,400)
        TextSurf105, TextRect105 = text_objects("of recovery will be doubled/tripled, and it will decrease when higher than maximum.", canteur25)
        TextRect105.center = (400,425)
        TextSurf106, TextRect106 = text_objects("The recovery is boosted by 5 times within 4 seconds of dealing any damage to your", canteur25)
        TextRect106.center = (400,450)
        TextSurf107, TextRect107 = text_objects("opponent. Your HP will recover at a rate of 2 per second, or 4 when it", canteur25)
        TextRect107.center = (400,475)
        TextSurf108, TextRect108 = text_objects("is lower than 15% your maximum. Your initial damage is 50 and can be improved.", canteur25)
        TextRect108.center = (400,500)
        TextSurf109, TextRect109 = text_objects("There will also be some boosters in the map, which provides buffs to players.(Future Function)", canteur25)
        TextRect109.center = (350,525)
        TextSurf110, TextRect110 = text_objects("Press [1] to start game, press [2] for main menu, press [3] to quit", canteur25)
        TextRect110.center = (420,625)
        #Creates all the tutorial texts
        
        gameDisplay.blit(TextSurf100, TextRect100)
        gameDisplay.blit(TextSurf101, TextRect101)
        gameDisplay.blit(TextSurf102, TextRect102)
        gameDisplay.blit(TextSurf103, TextRect103)
        gameDisplay.blit(TextSurf104, TextRect104)
        gameDisplay.blit(TextSurf105, TextRect105)
        gameDisplay.blit(TextSurf106, TextRect106)
        gameDisplay.blit(TextSurf107, TextRect107)
        gameDisplay.blit(TextSurf108, TextRect108)
        gameDisplay.blit(TextSurf109, TextRect109)
        gameDisplay.blit(TextSurf110, TextRect110)
        #Make all the texts on the screen
        
        pygame.display.update()
        #Makes all changes to take effect


def game_over(winner):
#Screen for game over
    canteur60 = pygame.font.Font("Fonts/CENTAUR.TTF", 60)
    canteur20 = pygame.font.Font("Fonts/CENTAUR.TTF", 25)
    #Defines fonts used in game over screen
    
    gameDisplay.fill(white)
    if winner == 1:
        TextSurf201, TextRect201 = text_objects("Player 1 has won the game!", canteur60)
    if winner == 2:
        TextSurf201, TextRect201 = text_objects("Player 2 has won the game!", canteur60)
    TextRect201.center = (400,350)
    #Display results based on the outcome
    TextSurf202, TextRect202 = text_objects("Press [1] to quit the game      Press [2] to restart the game", canteur20)
    TextRect202.center = (300,600)
    gameDisplay.blit(TextSurf201, TextRect201)
    gameDisplay.blit(TextSurf202, TextRect202)
    #Display and make all other texts on this screen

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                pygame.quit()
                quit()
            #If [X] is pressed, quit the game

            if event.key == pygame.K_2:
                main()

    pygame.display.update()
    #Update the screen to let it take effect
    


def main():
#Main program
    movingsprites = pygame.sprite.Group()
    player1 = Player(392,20,red)
    movingsprites.add(player1)
    player2 = Player(392,570,dyellow)
    movingsprites.add(player2)
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

    t_m = 0
    t_s0 = "0"
    t_s = 0
    SecondCounter = 1
    #Initialises variables for clock

    GameExit = False
    #Initialises main loop terminaition variable
    
    while not GameExit:
    #Event processing starts here
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                GameExit = True
            #Quit the game if the user chose to do so.

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    player1.changespeed(-5,0)
                if event.key == pygame.K_d:
                    player1.changespeed(5,0)
                if event.key == pygame.K_w:
                    player1.changespeed(0,-5)
                if event.key == pygame.K_s:
                    player1.changespeed(0,5)
                #When a direction key is pressed let player1 to do according movements

                if event.key == pygame.K_j:
                    player2.changespeed(-5,0)
                if event.key == pygame.K_l:
                    player2.changespeed(5,0)
                if event.key == pygame.K_i:
                    player2.changespeed(0,-5)
                if event.key == pygame.K_k:
                    player2.changespeed(0,5)
                #When a direction key is pressed let player2 to do according movements

                if event.key == pygame.K_1:
                    start_menu()
                #When M is pressed go back to main game menu

                if event.key == pygame.K_2:
                    pygame.quit()
                    quit()
                #When V is pressed quit the game

                if event.key == pygame.K_3:
                    tutorial()
                #When H is pressed go to tutorial

                if event.key == pygame.K_c:
                    if (player1.get_change_x() != 0) or (player1.get_change_y() != 0):
                        if player1.get_mp() >= 60:
                            player1.shoot()
                #If shooting key for player1 is pressed and player1 meets all requirements to shoot

                if event.key == pygame.K_n:
                    if (player2.get_change_x() != 0) or (player2.get_change_y() != 0):
                        if player2.get_mp() >= 60:
                            player2.shoot()
                #If shooting key for player2 is pressed and player2 meets all requirements to shoot

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    player1.changespeed(5,0)
                if event.key == pygame.K_d:
                    player1.changespeed(-5,0)
                if event.key == pygame.K_w:
                    player1.changespeed(0,5)
                if event.key == pygame.K_s:
                    player1.changespeed(0,-5)
                #When a direction key is released reset player1's speed

                if event.key == pygame.K_j:
                    player2.changespeed(5,0)
                if event.key == pygame.K_l:
                    player2.changespeed(-5,0)
                if event.key == pygame.K_i:
                    player2.changespeed(0,5)
                if event.key == pygame.K_k:
                    player2.changespeed(0,-5)
                #When a direction key is released reset player2's speed

        for bullet in bullet_list:
            bullet.move()
        #Updates positions of all bullets on the screen

        #Event processing ends here

        #Additional drawing starts here

        gameDisplay.fill(white)
        #Fills the entire window with white to initialise

        movingsprites.draw(gameDisplay)
        bullet_list.draw(gameDisplay)
        current_map.wall_list.draw(gameDisplay)
        #Draws all sprites and walls
        
        centaur15 = pygame.font.Font("Fonts/CENTAUR.TTF", 15)
        centaur20 = pygame.font.Font("Fonts/CENTAUR.TTF", 20)
        centaur35 = pygame.font.Font("Fonts/CENTAUR.TTF", 35)
        #Defines fonts used in main game loop

        TextSurf5, TextRect5 = text_objects("Press [1] to go to game menu    Press [2] to quit the game    Press [3] for tutorial", centaur20)
        TextRect5.center = (300,680)
        gameDisplay.blit(TextSurf5, TextRect5)
        #Displays text for going back to main menu or quit the game

        TextSurf6, TextRect6 = text_objects("Player1 HP:" + str(player1.get_hp()) + "/" + str(player1.get_max_hp()), centaur20)
        TextRect6.center = (85,625)
        gameDisplay.blit(TextSurf6, TextRect6)
        #Displays information of the hp remaining of player1

        TextSurf7, TextRect7 = text_objects("Player1 MP:" + str(player1.get_mp()) + "/1000", centaur20)
        TextRect7.center = (90,650)
        gameDisplay.blit(TextSurf7, TextRect7)
        #Displays information of the mp remaining of player2

        TextSurf8, TextRect8 = text_objects("Player2 HP:" + str(player2.get_hp()) + "/" + str(player2.get_max_hp()), centaur20)
        TextRect8.center = (715,625)
        gameDisplay.blit(TextSurf8, TextRect8)
        #Displays information of the hp remaining of player2

        TextSurf9, TextRect9 = text_objects("Player2 MP:" + str(player2.get_mp()) + "/1000", centaur20)
        TextRect9.center = (705,650)
        gameDisplay.blit(TextSurf9, TextRect9)
        #Displays information of the mp remaining of player2

        TextSurf10, TextRect10 = text_objects("Game Time", centaur15)
        TextRect10.center = (400,620)
        TextSurf11, TextRect11 = text_objects(str(t_m) + ":" + t_s0 + str(t_s), centaur35)
        TextRect11.center = (400,640)
        gameDisplay.blit(TextSurf10, TextRect10)
        gameDisplay.blit(TextSurf11, TextRect11)
        #Displays time information of the game

        #Additional drawing stops here

        pygame.sprite.groupcollide(bullet_list,current_map.wall_list,True,False)
        #If a bullet hit a wall, make the bullet dissappear

        player1.move(current_map.wall_list)
        #Updates the position of player1 in each tick

        player2.move(current_map.wall_list)
        #Updates the position of player2 in each tick

        player1.mp_update()
        #Updates the mp of player1 in each tick

        player2.mp_update()
        #Updates the mp of player2 in each tick

        player1.hp_recovery()
        #Updates the hp of player1

        player2.hp_recovery()
        #Uodates the hp of player2

        if player1.get_hp() < 0:
            game_over(2)
            player1.hp_change(-10000)
        elif player2.get_hp() < 0:
            game_over(1)
            player2.hp_change(-10000)
        #If any player died, terminate the game

        #clock_update(t_m, t_s0, t_s, SecondCounter)
        #Updates the clock

        if SecondCounter == 30:
            t_s = t_s + 1
            SecondCounter = 0
        else:
            SecondCounter = SecondCounter + 1
        #Increment second display when needed
        
        if t_s == 60:
            t_m = t_m + 1
            t_s = 0
        #Increment minute display when needed

        if t_s < 10:
            t_s0 = "0"
        else:
            t_s0 = ""
        #When seconds is only 1 digit add another 0

        pygame.display.update()
        #Updates the game window
        
        clock.tick(30)
        #Sets game frame rate to 30

    pygame.quit()
    #Quit the game when the game is no longer inside the main loop

if __name__ == "__main__":
    start_menu()
    tutorial()
    main()
#Calls main menu at the start of the game
