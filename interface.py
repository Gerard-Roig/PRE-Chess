import pygame
import board

class Interface:
    def __init__(self, win):
        self.win=win
        self.width, self.height = self.win.get_size()
        self.board = board.Board(self.win)

        self.bmargin = 0.1 # board margin to window (%)

    def update(self):
        self.width, self.height = self.win.get_size()


    def main_menu(self):
        return

    def game(self):

        return