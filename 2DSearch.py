import pygame


''' Main class to run program '''
class Main:

    global win_title  # window title
    win_title = '2DSearch'
    global win_dims  # default window dimensions
    win_dims = (1000, 700)

    def __init__(self):
        pygame.init()  # initializes pygame

        pygame.display.set_caption(win_title)  # sets window title
        surface = Surface(win_dims, (40, 40, 40))  # creates a surface
        pygame.display.flip()
        surface.build_grid(25)

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

    surface = None

    def __init__(self, surface_dims: (int, int), fill_color: (int, int, int)):
        self.surface = pygame.display.set_mode(surface_dims)  # creates a surface
        self.surface.fill(fill_color)  # sets surface fill color

    ''' Builds a grid of rectangular nodes in columns from left->right '''
    def build_grid(self, node_dims: int):
        node_size = node_dims  # Set the size of the grid block
        for x in range(win_dims[0] // node_size):
            for y in range(8, win_dims[1] - 100 // node_size):
                node = pygame.Rect(x * node_size, y * node_size,
                                   node_size, node_size)
                pygame.draw.rect(self.surface, (200, 0, 220), node, 1)
            pygame.time.delay(40)
            pygame.display.flip()


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