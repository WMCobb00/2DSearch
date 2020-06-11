import pygame
import random


''' Main class to run program '''
class Main:

    global win_title  # window title
    win_title = '2DSearch'
    global win_dims  # default window dimensions
    win_dims = (1000, 700)

    def __init__(self):
        pygame.init()  # initializes pygame

        pygame.display.set_caption(win_title)  # sets window title
        canvas = pygame.display.set_mode(win_dims)  # creates a surface
        canvas.fill((255, 255, 255))  # sets the surface color
        pygame.display.update()

        node_size = 25  # Set the size of the grid block
        for x in range(win_dims[0]//node_size):
            for y in range(8, win_dims[1]-100//node_size):
                rect = pygame.Rect(x * node_size, y * node_size,
                                   node_size, node_size)
                pygame.draw.rect(canvas, (100, 50, 100), rect, 1)
        pygame.display.update()

        ''' Main loop '''
        run = True
        while run:
            pygame.time.delay(100)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
        pygame.quit()


''' Creates a new Pygame Surface '''
class Canvas:

    canvas = None

    def __init__(self, canvas_dims: (int, int), fill_color: (int, int, int)):
        self.build_canvas(canvas_dims, fill_color)


    def build_canvas(self, canvas_dims: (int, int), fill_color: (int, int, int)):
        self.canvas = pygame.display.set_mode(canvas_dims)
        self.canvas.fill(fill_color)

        return self.canvas

    ''' Method to draw a block grid on screen '''
    def draw_grid(self):
        node_size = 20  # Set the size of the grid block
        for x in range(self.win_dims[0]):
            for y in range(self.win_dims[1]):
                rect = pygame.Rect(x * node_size, y * node_size,
                                   node_size, node_size)
                pygame.draw.rect(self.surface, (100, 100, 100), rect, 1)


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