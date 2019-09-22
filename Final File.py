import pygame

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
    #initiates player's speed
    
    def __init__(self,x,y):
    #constructor
        pygame.sprite.Sprite.__init__(self)
        #Call the parent's constructor

        self.image = pygame.Surface([15,15]) 
        self.image.fill(yellow)
        #Sets height, width and colour of the tank

        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
        #Make the top-left corner of the "tank" the passed-in location

    def changespeed(self,x,y):
    #Changes the speed of the player when related keys are pressed
        self.change_x += x
        self.change_y += y

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

class Map():
#Base class for all maps

    wall_list = None
    enemy_sprites = None

    def __init__(self):
    #Constructor
        self.wall_list = pygame.sprite.Group()
        self.enemy_sprites = pygame.sprite.Group()

class M_Classic(Map):
#Class for map M_Classic
    def __init__(self):
        Map.__init__(self)
        #Calls the constructor of its parent class

        walls = [ [0,0,10,600,brown],
                  [0,0,800,10,brown],
                  [790,000,10,600,brown],
                  [0,590,800,10,brown]
                ]
        #This is the list of walls in map "M_Classic"

        for item in walls:
            wall = Wall(item[0],item[1],item[2],item[3],item[4])
            self.wall_list.add(wall)
        #Actually adds all the walls


def main():
#Main program
    pygame.init()
    #initiates pygame

    display_width = 800
    display_height = 600
    gameDisplay = pygame.display.set_mode([display_width,display_height])
    #Sets resolution of the game window and actually creates it

    pygame.display.set_caption('TryHard MazeGame V0.3.0 (22-SEP-19)')
    #Sets title of the game window

    player = Player(390,30)
    movingsprites = pygame.sprite.Group()
    movingsprites.add(player)
    #Creates the player and adds it into the sprite list

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

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.changespeed(-5,0)
                if event.key == pygame.K_RIGHT:
                    player.changespeed(5,0)
                if event.key == pygame.K_UP:
                    player.changespeed(0,-5)
                if event.key == pygame.K_DOWN:
                    player.changespeed(0,5)

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    player.changespeed(5,0)
                if event.key == pygame.K_RIGHT:
                    player.changespeed(-5,0)
                if event.key == pygame.K_UP:
                    player.changespeed(0,5)
                if event.key == pygame.K_DOWN:
                    player.changespeed(0,-5)
        #Event processing ends here

        #Game logic starts here

        #Game logic ends here

        gameDisplay.fill(white)
        #Fills the entire window with white
        
        movingsprites.draw(gameDisplay)
        current_map.wall_list.draw(gameDisplay)
        #Draws all sprites and walls
        
        pygame.display.flip()
        #Updates the game window
        
        clock.tick(30)
        #Sets game frame rate to 30

    pygame.quit()

if __name__ == "__main__":
    main()
