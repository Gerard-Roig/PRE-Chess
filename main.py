import pygame

# Constants
WIDTH, HEIGHT = 640,360  # Board size
wRATIO = HEIGHT/WIDTH
hRATIO = 1
WHITE = (238, 238, 210)
BLACK = (118, 150, 86)

# Initialize pygame
pygame.init()
WIN = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("Chess Board")

def updateRATIO(max):
    global wRATIO, hRATIO
    global WIDTH, HEIGHT
    wRATIO, hRATIO = (HEIGHT/WIDTH, 1) if max else (1, WIDTH/HEIGHT)
    print(wRATIO, hRATIO)

def drawSquare(x,y,s):
    global wRATIO, hRATIO
    x=round(x*WIDTH)
    y=round(y*HEIGHT)
    w=round(s*WIDTH*wRATIO)
    h=round(s*HEIGHT*hRATIO)
    return pygame.Rect(x,y,w,h)

def drawBoard():
    global wRATIO, hRATIO
    a=0
    for j in range(1,9):
        for i in range(1,9):
            col = BLACK if (i+a)% 2 == 0 else WHITE
            pygame.draw.rect(WIN,col,drawSquare((i-1)/8*wRATIO,(j-1)/8*hRATIO, 1/8))
        a=a+1

def main():
    global WIN, WIDTH,HEIGHT
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            # Handle window resizing
            if event.type == pygame.VIDEORESIZE:
                after = event.w > event.h
                before = WIDTH > HEIGHT
                WIDTH,HEIGHT = pygame.display.get_window_size()
                WIN = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE) # Update window size
                updateRATIO(after)
                drawBoard()
        drawBoard()
        

        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()