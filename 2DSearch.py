import tkinter as tk

''' Main class to run program '''
class Main:

    global win_title  # window title
    win_title = '2DSearch'
    global win_dims  # default window dimensions
    win_dims = (1000, 700)

    def __init__(self):
        pygame.init()  # initializes pygame

        pygame.display.set_caption(win_title)  # sets window title
        Grid(win_dims, 25, (200, 0, 220))  # creates a surface
        pygame.display.flip()

        ''' Main loop '''
        run = True
        while run:
            pygame.time.delay(100)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
        pygame.quit()


''' Creates a new Pygame Surface '''
class Surface:

    def __init__(self, surface_dims: (int, int)):
        self.surface = pygame.display.set_mode(surface_dims)  # creates a surface
        self.surface.fill((40, 40, 40))  # sets surface fill color to 'dark grey'

        # NEED TO HAVE A MENU BUILT HERE


''' Creates a Grid type subclass of Surface'''
class Grid(Surface):

    def __init__(self, surface_dims: (int, int), node_size: int, grid_color: (int, int, int)):
        super(Grid, self).__init__(surface_dims)
        self.grid_matrix = [[]]

        self.build_grid(node_size, grid_color)

    ''' Builds a grid of rectangular nodes in columns from left->right '''
    def build_grid(self, node_size: int, grid_color: (int, int, int)):
        self.build_grid_matrix(node_size)  # builds a matrix of the grid

        for x in range(win_dims[0] // node_size):
            for y in range(8, win_dims[1] - 100 // node_size):
                node = pygame.Rect(x * node_size, y * node_size,
                                   node_size, node_size)
                pygame.draw.rect(self.surface, grid_color, node, 1)
            pygame.time.delay(35)
            pygame.display.flip()

    ''' Builds a matrix of int values to control displayed grid '''
    def build_grid_matrix(self, node_size: int):
        for x in range(win_dims[0] // node_size):
            self.grid_matrix[0].append(0)
        for y in range(8, win_dims[1] - 100 // node_size):
            self.grid_matrix.append(self.grid_matrix[0])


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