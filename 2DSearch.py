'''
**********************
Author: William Cobb
Project: 2DSearch
Created on: 6/14/2020
**********************
'''

import tkinter as tk
from PIL import Image, ImageTk
from time import sleep


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
    __title_img = Image.open('.//resources//images//2DSearchTitle.png')
    __logo_img = Image.open('.//resources//images//2DSearchLogo.png')
    __search_methods = ['Depth First Search', 'Breadth First Search', "Djikstra's", 'A*', 'Greedy Best First Search']


    def __init__(self):

        self.root = tk.Tk()  # Builds root window for this App instance

    #  Driver method for App class
    def run_app(self):

        self.__build_app_root()
        self.__build_app_children()
        # Insert Code here

        self.root.mainloop()

    #  Builds root
    def __build_app_root(self):

        self.root.title(App.__win_title)
        self.root.iconbitmap('.//resources//images//icons//2DSearch.ico')  # Sets window icon
        self.root.minsize(App.__win_dims[0], App.__win_dims[1])
        self.root.resizable(False, False)
        self.root.configure(bg='#A4A4A4')  # Sets window bg color

    def __build_app_children(self):

        #  Title
        '''title_art = tk.Label(self.root, image=ImageTk.PhotoImage(App.__title_img))
        title_art.photo = ImageTk.PhotoImage(App.__title_img)
        title_art.pack()'''

        # Search and tutorial buttons  https://www.tutorialspoint.com/python/tk_button.htm
        search = tk.Button(self.root, text='Search!', fg='purple', activeforeground='purple', command=None)
        search.place(anchor=tk.CENTER, x=600, y=100, height=50, width=100)

        tutorial = tk.Button(self.root, text='Tutorial', fg='purple', activeforeground='purple', command=None)
        tutorial.place(anchor=tk.CENTER, x=600, y=210, height=30, width=75)

        # Speed scale  https://www.tutorialspoint.com/python/tk_scale.htm
        speed_scale = tk.Scale(self.root, variable=tk.DoubleVar, orient=tk.HORIZONTAL, length=200,
                         label='Search speed', activebackground='purple', fg='purple', from_=1, to=4,
                         tickinterval=1, showvalue=0)
        speed_scale.place(anchor=tk.CENTER, x=950, y=100)

        # Search method listbox  https://www.tutorialspoint.com/python/tk_listbox.htm
        search_list = tk.Listbox(self.root, height=5, width=30, fg='purple', selectbackground='purple')
        for method in App.__search_methods:
            search_list.insert(tk.END, method)
        search_list.place(anchor=tk.CENTER, x=250, y=105)

        # Grid canvas  https://www.tutorialspoint.com/python/tk_canvas.htm
        grid_canvas = tk.Canvas(self.root, width=App.__win_dims[0], height=App.__win_dims[1])
        grid_canvas.place(y=225)

    #  App class to_string method
    def to_string(self):

        return f'Window title: {App.__win_title}\nWindow dimensions: {App.__win_dims}\n' \
            f'Window Type: {type(self.root)}'


''' Grid class to build and update both the visual grid and the control matrix '''

class Grid():

    def __init__(self):
        pass


''' Node class to build interactive nodes '''

class Node():

    def __init__(self):
        pass


if __name__ == '__main__':
    Main()