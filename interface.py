import pygame
import board

class Interface:
    def __init__(self, win):
        self.win=win

        self.b_img = pygame.image.load("board.png").convert_alpha() # board image
        self.b_pos = (0, 0) # board top-left corner position
        self.b_size = 0.6 # board size relative to window (%)
        self.b_margin = 0.1 # board margin to window (%)

    def update(self):
        return




    def main_menu(self):
        return

    def game(self):

        return

    def draw_board(self):
        self.b_pos= self.win.get_size()*self.b_margin

        b_dim= self.win.getsize()*(9/16, 1)

        self.b_img = pygame.transform.scale(self.b_img, b_dim)  # Resize the image (optional)

        self.win.blit(self.b_img, self.b_pos)
