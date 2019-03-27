import pygame
##import the necessary libraries
from balloon import Balloon
##import the sprite object
pygame.init()
## initializes the pygame engine

# Define some colors
BLACK = ( 0, 0, 0)
WHITE = ( 255, 255, 255)
GREEN = ( 0, 255, 0)
RED = ( 255, 0, 0)
SKYBLUE = ( 135, 206, 235)
# Open a new window
SCREENX = 500
SCREENY = 820
size = (SCREENX, SCREENY)
##(width, vertical length)
## sets size of the display
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Balloon Concentration") ##Header for the game

##There are three parts to any pygame engine

##Capturing Events: Used to constantly “listen” to user inputs and react to these. It could be when the user use
#  the keyboard or the mouse.

# Implementing the Game Logic. What happens when the game is running? Are cars moving forward, aliens falling from
# the sky, ghosts chasing you, etc.

# Refreshing the screen by redrawing the stage and the sprites.



#This will be a list that will contain all the sprites we intend to use in our game.
all_sprites_list = pygame.sprite.Group()
playerB = Balloon(RED, 112, 130)
playerB.rect.x = SCREENX/6
playerB.rect.y = SCREENY/3
##Even though its an ellipse, it must be called as a rect


# Add the balloon to the list of objects
all_sprites_list.add(playerB)


# The loop will carry on until the user exit the game (e.g. clicks the close button).
carryOn = True


# The clock will be used to control how fast the screen updates
clock = pygame.time.Clock()

# -------- Main Program Loop -----------
while carryOn:
    # --- Main event loop
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
              carryOn = False # Flag that we are done so we exit this loop

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and playerB.rect.y> 0:
        playerB.moveUp(5)

 # --- Game logic should go here
    ##where each time the frame updates itself
    all_sprites_list.update()
    if playerB.rect.y <= 650:
        playerB.moveDown(2.5)

    # --- Drawing code should go here
    # First, clear the screen to white.
    screen.fill(SKYBLUE)

    # The you can draw different shapes and lines or add text to your background stage.
   # pygame.draw.rect(screen, RED, [55, 200, 100, 70], 10)
    ##for all positive integers
    ##[right, down, width, length], border]
    #pygame.draw.line(screen, GREEN, [0, 0], [100, 100], 5)
    ##Top[x,y] Bottom[x,y]
  ##  pygame.draw.ellipse(screen, BLACK, [90, 20, 250, 100], 2)

    # Now let's draw all the sprites in one go. (For now we only have 1 sprite!)
    all_sprites_list.draw(screen)

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Once we have exited the main program loop we can stop the game engine:
pygame.quit()