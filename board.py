import pygame

class Board:
    def __init__(self, win, w, h):

        self.win = win

        self.width = w
        self.height = h

        self.wRATIO = self.height/self.width
        self.hRATIO = self.width/self.height

        self.white = (238, 238, 210)
        self.black = (118, 150, 86)

    def update_ratio(self, win):
        self.win = win
        size=(self.width,self.height)
        ratio = min(size)/max(size)
        (self.wRATIO, self.hRATIO)= (ratio, 1) if max(size)==self.width else (1, ratio)

    def resize(self, w, h, win):
        self.width = w
        self.height = h
        self.update_ratio(win)

    def drawSquare(self, x, y, s):
        x=round(x*self.width)
        y=round(y*self.height)
        w=round(s*self.width*self.wRATIO)
        h=round(s*self.height*self.hRATIO)
        return pygame.Rect(x,y,w,h)

    def drawBoard(self):
        a=0
        for j in range(1,9):
            for i in range(1,9):
                col = self.black if (i+a)% 2 == 0 else self.white
                pygame.draw.rect(self.win,col,self.drawSquare((i-1)/8*self.wRATIO,(j-1)/8*self.hRATIO, 1/8))
            a=a+1

    #si width es mes gran volem obtenir height -> height/width