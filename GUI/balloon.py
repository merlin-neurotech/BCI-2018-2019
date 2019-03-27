import pygame

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


class Balloon(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        # Call the parent class (Sprite) constructor
        super().__init__()

        # Pass in the color of the car, and its x and y position, width and height.
        # Set the background color and set it to be transparent
        self.image = pygame.Surface([width, height])
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)

        # Draw the balloon (an ellipse!)
        #  pygame.draw.ellipse(self.image, color, [0, 0, width, height])

        # Instead we could load a proper pciture of a balloon...
        self.image = pygame.image.load("balloon.png").convert_alpha()

        # Fetch the rect object that has the dimensions of the image.
        self.rect = self.image.get_rect()
        ##Even though its an ellipse, it must be called as a rect

    def moveUp(self, pixels):
        self.rect.y -= pixels

    def moveDown(self, pixels):
        self.rect.y += pixels
