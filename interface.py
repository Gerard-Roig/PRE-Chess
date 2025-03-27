import pygame

class Interface:
    def __init__(self, win):
        self.win=win

        self.b_img = pygame.image.load("board.png").convert_alpha() # board image
        self.b_pos = (0, 0) # tuple - board top-left corner position
        self.b_size = 0.9 # board size relative to window height (%)
        self.b_margin = 0.05 # board margin to window height (%)

    def update(self):
        return




    def main_menu(self):
        return

    def game(self):

        return

    def draw_board(self):
        #defining position coords
        #b_x, b_y= self.win.get_size() # get window size (for any resizing)
        b_m= self.win.get_size()[1]*self.b_margin # take the percentage for the margin

        #defining board size
        b_dim= self.win.get_size() # get window size (for any resizing)
        b_s = b_dim[1]*self.b_size # takes percentage of screen size, also adjusts size with ratio for it to be a square

        board = pygame.transform.scale(self.b_img, (b_s, b_s))  # actual resizing of the image, with adjusted size

        self.round_corners(board, round(b_m*(0.01/0.05))) # round corners -> 1% of screen height

        self.win.blit(board, (b_m, b_m)) # draw the board on top-left corner coords

        
    
    def round_corners(self, img, r):
         # Create a transparent mask surface
        mask = pygame.Surface(img.get_size(), pygame.SRCALPHA)

        # Draw a rounded rectangle on the mask
        pygame.draw.rect(mask, (255, 255, 255, 255), mask.get_rect(), border_radius=r)

        # Apply the rounded mask to the image
        img.blit(mask, (0, 0), special_flags=pygame.BLEND_RGBA_MIN)
