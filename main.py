import pygame
import board

# Constants
WIDTH, HEIGHT = 640,360  # Board size
RATIO = 16/9
WHITE = (238, 238, 210) # Unused
BLACK = (118, 150, 86) # Unused

# Initialize pygame
pygame.init()
WIN = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("Chess Board")

board = board.Board(WIN)


def main():
    global WIN, WIDTH,HEIGHT
    run = True
    board.draw()
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            # Handle window resizing
            if event.type == pygame.VIDEORESIZE:
                WIDTH,HEIGHT = pygame.display.get_window_size()
                WIDTH = HEIGHT*RATIO
                WIN = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE) # Update window size

                board.draw()

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()