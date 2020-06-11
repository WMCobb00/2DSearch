import pygame
import random

''' Main class to run program '''
class Main:

    def __init__(self):
        pygame.init()  # initializes pygame
        screen = UI()  # creates a new window

        ''' Main loop '''
        run = True
        while run:
            pygame.time.delay(100)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
        pygame.quit()

''' Creates a UI '''
class UI:

    win = pygame.display  # defines window
    title = '2DSearch'  # window caption
    win_dims = (1000, 600)  # sets default window dimensions
    surface = pygame.Surface(win_dims)

    def __init__(self):
        self.win.set_caption(self.title, self.title)
        self.win.set_mode(self.win_dims)


    ''' Method to draw a block grid on screen '''
    def draw_grid(self):
        blockSize = 20  # Set the size of the grid block
        for x in range(self.win_dims[0]):
            for y in range(self.win_dims[1]):
                rect = pygame.Rect(x * blockSize, y * blockSize,
                                   blockSize, blockSize)
                pygame.draw.rect(self.win, (0, 0, 0), rect, 1)

class Search:
    pass

class DFS(Search):
    pass

class BFS(Search):
    pass

class Djikstra(Search):
    pass

class AStar(Search):
    pass

if __name__ == '__main__':
    Main()