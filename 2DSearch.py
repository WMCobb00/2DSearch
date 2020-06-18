'''
**********************
Author: William Cobb
Project: 2DSearch
Created on: 6/14/2020
**********************
'''

import tkinter as tk
from PIL import Image, ImageTk


''' Main class to run program '''

class Main:

    def __init__(self):

        app = App()
        app.run_app()


''' App class to build the GUI '''

class App:

    # App vars
    __win_title = '2DSearch'
    __win_dims = (1200, 700)

    def __init__(self):

        self.root = tk.Tk()  # Builds root window for this App instance

    #  Driver method for App class
    def run_app(self):

        self.__build_app_root()
        self.__title_screen()

        # Insert Code here

        self.root.mainloop()

    #  Builds root
    def __build_app_root(self):
        self.root.title(App.__win_title)
        self.root.iconbitmap('./resources/images/icons/2DSearch.ico')  # Sets window icon
        self.root.minsize(App.__win_dims[0], App.__win_dims[1])
        self.root.resizable(False, False)
        self.root.configure(bg='#A4A4A4')  # Sets window bg color

    #  Title screen animation
    def __title_screen(self):
        canvas = tk.Canvas(self.root, width=App.__win_dims[0], height=App.__win_dims[1])
        canvas.pack(expand=True, fill='both')

        canvas.create_image(200, 200, image=tk.PhotoImage(file='./resources/images/2DSearch.png'), anchor='center')

    def __tutorial_screen(self):
        pass

    def __main_screen(self):
        pass

    # App class to_string method
    def to_string(self):
        return f'Window title: {App.__win_title}\nWindow dimensions: {App.__win_dims}\n' \
            f'Window Type: {type(self.root)}'


''' Grid class to build and update both the visual grid and the control matrix '''

class Grid:

    def __init__(self):
        pass


''' Parent search class '''

class Search:

    def __init__(self):
        pass


''' Depth First Search '''

class DFS(Search):

    def __init__(self):
        pass


''' Breadth First Search '''

class BFS(Search):

    def __init__(self):
        pass


''' Djikstra's Algorithm '''

class Djikstra(Search):

    def __init__(self):
        pass


''' A* Search Algorithm '''

class AStar(Search):

    def __init__(self):
        pass


''' Greedy Best First Search Algorithm '''

class GBFS(Search):

    def __init__(self):
        pass


if __name__ == '__main__':
    Main()