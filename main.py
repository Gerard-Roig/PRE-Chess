import pygame
import interface as win

# Constants
WIDTH, HEIGHT = 640,360  # Board size
RATIO = 16/9
WHITE = (238, 238, 210) # Unused
BLACK = (118, 150, 86) # Unused
BACKGROUND = (48, 46, 43)

# Initialize pygame
pygame.init()
WIN = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("Chess Board")

interface=win.Interface(WIN)


def main():
    global WIN, WIDTH,HEIGHT
    WIN.fill(BACKGROUND)
    run = True
    interface.draw_board()
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            # Handle window resizing
            if event.type == pygame.VIDEORESIZE:
                WIDTH,HEIGHT = pygame.display.get_window_size()
                WIDTH = HEIGHT*RATIO
                WIN = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE) # Update window size

                WIN.fill(BACKGROUND)
                interface.draw_board()

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()