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



class App:
    '''
        App class to serve as the app foundation. Includes root, window, and child objects as well as the driver method
    '''

    # Static App vars
    __win_title = '2DSearch'
    __win_dims = (1200, 700)
    __title_img = Image.open('.//resources//images//2DSearchTitle.png')
    __logo_img = Image.open('.//resources//images//2DSearchLogo.png')
    __search_methods = ['Depth First Search', 'Breadth First Search', "Djikstra's", 'A*', 'Greedy Best First Search']


    def __init__(self):
        '''
        App constructor
        '''

        self.root = tk.Tk()  # Builds root window for this App instance
        
        # Children
        self.title_art = None
        self.search = None
        self.tutorial = None
        self.speed_scale = None
        self.grid = None
        self.search_method_list = None


    def run_app(self):
        '''
        Driver method for App
        '''

        self.__define_root_props()
        self.__define_child_props()
        # Insert Code here
        
        self.root.mainloop()


    def __define_root_props(self):
        '''
        defines root properties
        '''

        self.root.title(App.__win_title)
        self.root.iconbitmap('.//resources//images//icons//2DSearch.ico')  # Sets window icon
        self.root.minsize(App.__win_dims[0], App.__win_dims[1])
        self.root.resizable(False, False)
        self.root.configure(bg='#A4A4A4')  # Sets window bg color


    def __define_child_props(self):                                     #  put all constructor statements in __init__
        '''
        defines the properties of the roots child widgets
        '''

        #  Title art
        '''self.title_art = tk.Label(self.root, image=ImageTk.PhotoImage(App.__title_img))
        self.title_art.photo = ImageTk.PhotoImage(App.__title_img)
        self.title_art.pack()'''

        # Search and tutorial buttons  https://www.tutorialspoint.com/python/tk_button.htm
        self.search = tk.Button(self.root, text='Search!', fg='purple', activeforeground='purple', command=None)
        self.search.place(anchor=tk.CENTER, x=600, y=100, height=50, width=100)

        self.tutorial = tk.Button(self.root, text='Tutorial', fg='purple', activeforeground='purple', command=None)
        self.tutorial.place(anchor=tk.CENTER, x=600, y=210, height=30, width=75)

        # Speed scale  https://www.tutorialspoint.com/python/tk_scale.htm
        self.speed_scale = tk.Scale(self.root, variable=tk.DoubleVar, orient=tk.HORIZONTAL, length=200,
                         label='Search Speed %', activebackground='purple', fg='purple', from_=1, to=100,
                         tickinterval=0, showvalue=1)
        self.speed_scale.set(50)
        self.speed_scale.place(anchor=tk.CENTER, x=950, y=100)

        # Search method listbox  https://www.tutorialspoint.com/python/tk_listbox.htm
        # var.get example may be useful here https://www.tutorialspoint.com/python/tk_scale.htm
        self.search_method_list = tk.Listbox(self.root, height=5, width=30, fg='purple', selectbackground='purple')
        for method in App.__search_methods:
            self.search_method_list.insert(tk.END, method)
        self.search_method_list.place(anchor=tk.CENTER, x=250, y=105)

        # Grid canvas  https://www.tutorialspoint.com/python/tk_canvas.htm
        self.grid = Grid(root=self.root, width=App.__win_dims[0], height=App.__win_dims[1])
        self.grid.place_canvas()


    def to_string(self):
        '''
        App class data to_string method
        '''

        return f'\nApp Properties:\nWindow Title: {App.__win_title}\nWindow Dimensions: {App.__win_dims}\n' \
            f'Window Type: {type(self.root)}'



class Grid():
    '''
        Grid class to build and update the visual grid
    '''


    def __init__(self, root: tk.Tk, width: int, height: int, y_offset_val: int=250):
        '''
        Grid constructor
        :param root: tk.Tk() object
        :param width: canvas width, use window width
        :param height: canvas height, use window height
        :param y_offset_val: canvas y axis offset from top of screen, offset=250 by default
        '''

        self.canvas_root = root
        self.canvas_width = width
        self.canvas_height = height
        self.y_offset = y_offset_val
        self.canvas = tk.Canvas(self.canvas_root, width=self.canvas_width, height=self.canvas_height)

        self.node_set = {}


    def place_canvas(self):
        '''
        Places a tk canvas in the window where Node objects can be drawn with the specified y offset
        '''

        self.canvas.place(y=self.y_offset)  # This gives us a x=1200, y=450 canvas to build a grid on
      

 
# useful https://stackoverflow.com/questions/3479265/help-creating-python-class-with-tkinter
class Node():
    '''
        Node class to build interactive tk canvas rectangles
    '''

    def __init__(self):
       self.coords = (100, 100, 200, 200)
       self.color = 'blue'


    def draw(self, my_canvas):
        """Draw the rectangle on a Tk Canvas."""
        my_canvas.create_rectangle(*self.coords, fill=self.color)



if __name__ == '__main__':
    app = App()
    app.run_app()
    print(type(Node()))
    print(app.to_string())