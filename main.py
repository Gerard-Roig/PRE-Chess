import pygame
import board

# Constants
"""
inicialització de les constants
WIDTH i HEIGHT son la resolucio de la finestra de l'aplicació (que volem que sigui variable en tamany, per tant veureu que aquestes variables son globals i es
van actualitzant i consultant constantment)

wRATIO i hRATIO son unes variables configurades per a fer conversions i poder tenir el tamany d'un quadrat. 
per exemple, wRATIO permet obtenir l'equivalent de l'alçada (height) a partir de l'amplada (width) multiplicant WIDTH*wRATIO (wRATIO = HEIGHT/WIDTH)
aquestes variables es van canviant amb la funcio updateRATIO() per tal que el taulell s'adapti a la mida de la pantalla i no sobresurti

L> Per tant quan el width sigui mes gran que el height, wRATIO valdra HEIGHT/WIDTH i hRATIO valdra 1, 
d'aquesta manera es podran crear rectangles de mida WIDTH*wRATIO (=HEIGHT) i HEIGHT*hRATIO (=HEIGHT), osigui quadrats.
I quan el HEIGHT sigui major, wRATIO sera 1 i hRATIO sera WIDTH/HEIGHT, per tant el taulell es formara de quadrats referents al WIDTH i s'adaptara al width (que es mes petit),
evitant aixi que s'adapti al HEIGHT i sobresurti de la pantalla
"""
WIDTH, HEIGHT = 640,360  # Board size
wRATIO = HEIGHT/WIDTH
hRATIO = 1
WHITE = (238, 238, 210)
BLACK = (118, 150, 86)

# Initialize pygame
pygame.init()
WIN = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("Chess Board")

board = board.Board(WIN, WIDTH, HEIGHT)


"""
def updateRATIO(max):
    
    assigna els valors del ratio i de 1 quan les mides canvien
    necessita com a argument un bool que confirmi si width>height
    
    global wRATIO, hRATIO
    global WIDTH, HEIGHT
    wRATIO, hRATIO = (HEIGHT/WIDTH, 1) if max else (1, WIDTH/HEIGHT)
    print(wRATIO, hRATIO)

def drawSquare(x,y,s):
    
    crea un quadrat amb mides percentuals (tant per 1) a partir de la funcio de crear rectangle
    arguments: 
    
    x - posició del costat esquerra del quadrat (percentual, tant per 1)

    y - posició del costat d'adalt del quadrat (percentual, tant per 1)

    s - mesura del costat del quadrat (percentual, tant per 1)

    exemple: drawSquare(0.15, 0.3 , 0.3) - crea un quadrat de costat un 30% de la mida més petita de la resolució (si width>height, ocupa 30% del height),
    situat a un 15% horitzontal i un 30% vertical de la pantalla (el 0,0 és en el corner top-left)

    
    global wRATIO, hRATIO
    x=round(x*WIDTH)
    y=round(y*HEIGHT)
    w=round(s*WIDTH*wRATIO)
    h=round(s*HEIGHT*hRATIO)
    return pygame.Rect(x,y,w,h)

def drawBoard():
    
    funció que crea un taulell de 8x8 quadrats amb els colors alternats (com un taulell d'escacs),
    adaptat percentualment a la pantalla
    
    global wRATIO, hRATIO
    a=0
    for j in range(1,9):
        for i in range(1,9):
            col = BLACK if (i+a)% 2 == 0 else WHITE
            pygame.draw.rect(WIN,col,drawSquare((i-1)/8*wRATIO,(j-1)/8*hRATIO, 1/8))
        a=a+1
"""

def main():
    global WIN, WIDTH,HEIGHT
    run = True

    board.resize(WIDTH, HEIGHT, WIN)
    board.drawBoard()

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            # Handle window resizing
            if event.type == pygame.VIDEORESIZE:
                WIDTH,HEIGHT = pygame.display.get_window_size()
                WIN = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE) # Update window size

                board.resize(WIDTH, HEIGHT, WIN)
                #       L>resize()
                #           L>updateRATIO(win)

                board.drawBoard()
        #drawBoard()
        

        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()