import pygame

class Board:
    def __init__(self, win):
        self.win = win
        self.width, self.height = self.win.get_size()
        self.image = pygame.image.load("board.png").convert_alpha()
        self.white = (238, 238, 210)
        self.black = (118, 150, 86)

    def draw(self):
        #resizes the image and draws it
        self.scale()
        self.win.blit(self.image, (0, 0))

#aquesta funció l'hauria de fer la classe ventana/interface
    def scale(self):
        #retreives new dimensions from window
        self.width, self.height = self.win.get_size()
        #scales them for the board to be a square
        self.width= self.height
        #resizes the image
        self.image = pygame.transform.scale(self.image, (self.width, self.height))  # Resize the image (optional)