'''
**********************
Author: William Cobb
Project: 2DSearch
Created on: 6/14/2020
**********************
'''

import tkinter as tk

''' Main class to run program '''

class Main:

    def __init__(self):
        pass


''' Window class to build the GUI '''

class Window:
    # Window vars
    __win_title = '2DSearch'
    __win_dims = (1200, 800)

    def __init__(self):
        pass

    # Scenes

    def main_menu(self):
        pass

    def tutorial(self):
        pass

    def app(self):
        pass


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