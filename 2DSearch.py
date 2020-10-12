'''
**********************
Author: William Cobb
Project: 2DSearch
Created on: 6/14/2020
Discription: An application to display 2D pathfinding algorithms
**********************
'''

import tkinter as tk
from PIL import Image, ImageTk
from time import sleep



class App:
    '''
        App class to serve as the app foundation. Includes root, window, and child objects as well as the driver method
    '''

    '''Static app vars'''
    __win_title = '2DSearch'
    __win_dims = (1205, 705)  # Dimensions end in 5 due to border padding in tk canvas
    __title_img = Image.open('.//resources//images//2DSearchTitle.png')
    __logo_img = Image.open('.//resources//images//2DSearchLogo.png')
    __search_methods = ['Depth First Search', 'Breadth First Search', "Djikstra's", 'A*', 'Greedy Best First Search']


    def __init__(self):
        '''
        App constructor
        '''

        '''root (aka window)'''
        self.root = tk.Tk()
        
        '''Child objects'''
        self.title_art = None
        self.search_button = tk.Button(self.root, text='Search!', fg='purple', activeforeground='purple', command=None)
        self.tutorial_button = tk.Button(self.root, text='Tutorial', fg='purple', activeforeground='purple', command=None)
        self.speed_mod_scale = tk.Scale(self.root, variable=tk.DoubleVar, orient=tk.HORIZONTAL, length=200,
                         label='Search Speed %', activebackground='purple', fg='purple', from_=1, to=100,
                         tickinterval=0, showvalue=1)
        self.search_method_list = tk.Listbox(self.root, height=5, width=30, fg='purple', selectbackground='purple')
        self.grid = Grid(root=self.root, width=App.__win_dims[0], height=App.__win_dims[1])


    def run_app(self):
        '''
        Driver method for App
        '''

        self.__define_root_props()
        self.__child_modifiers()
        # Insert Code here
        
        self.root.mainloop()


    def __define_root_props(self):
        '''
        Defines root properties
        '''

        self.root.title(App.__win_title)
        self.root.iconbitmap('.//resources//images//icons//2DSearch.ico')  # Sets window icon
        self.root.minsize(App.__win_dims[0], App.__win_dims[1])
        self.root.resizable(False, False)
        self.root.configure(bg='#A4A4A4')  # Sets window bg color


    def __child_modifiers(self):
        '''
        Modifies the properties of the roots child widgets
        '''

        '''Title art'''
        '''self.title_art = tk.Label(self.root, image=ImageTk.PhotoImage(App.__title_img))
        self.title_art.photo = ImageTk.PhotoImage(App.__title_img)
        self.title_art.pack()'''

        '''Search button'''
        self.search_button.place(anchor=tk.CENTER, x=600, y=100, height=50, width=100)

        '''Tutorial button'''
        self.tutorial_button.place(anchor=tk.CENTER, x=600, y=210, height=30, width=75)

        '''Speed modifier scale'''
        self.speed_mod_scale.set(50)
        self.speed_mod_scale.place(anchor=tk.CENTER, x=950, y=100)

        '''Search method listbox (preferably a dropdown at a later date)'''
        for method in App.__search_methods:
            self.search_method_list.insert(tk.END, method)
        self.search_method_list.place(anchor=tk.CENTER, x=250, y=105)

        '''Grid'''
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


    def __init__(self, root: tk.Tk, width: int, height: int, y_offset_val: int=240):
        '''
        Grid constructor
        :param root: tk.Tk() object
        :param width: canvas width, use window width
        :param height: canvas height, use window height
        :param y_offset_val: canvas y axis offset from top of screen, offset=260 by default
        '''

        self.canvas_root = root
        self.canvas_width = width
        self.canvas_height = height
        self.y_offset = y_offset_val
        self.x_offset = 0
        self.canvas = tk.Canvas(self.canvas_root, width=self.canvas_width-4, height=self.canvas_height-self.y_offset-4)

        self.node_list = []
        self.__fill_node_list()
        self.__draw_grid()


    def place_canvas(self):
        '''
        Places a tk canvas in the window where Node objects can be drawn with the specified y offset
        '''

        self.canvas.place(y=self.y_offset, x=self.x_offset)  # This gives us a x=1200, y=460 canvas to build a grid on (60x23 Nodes)


    def __fill_node_list(self):

        for i in range(0, int((1200/Node.node_width)*(460/Node.node_height)+1)):
            self.node_list.append(Node())

    
    def __draw_grid(self):

        for i in self.node_list:
            print(i.node_coords)
            i.draw(self.canvas)
      

 
class Node():                                                # Currently having issue where instance vars update when static vars do
    '''
        Node class to build interactive tk canvas rectangles
    '''

    '''Static node vars'''
    __next_node_id = 0
    node_height = 20
    node_width = 20
    __next_node_coords = [-18, 2, 2, 22]


    def __init__(self):
        '''
            Node constructor
        '''

        self.node_id = Node.__next_node_id
        self.node_coords = Node.__next_node_coords
        self.default_color = ''
        self.outline_color = '#4f4f4f'  # Dark grey
        self.hover_color = '#deaff3'  # Lilac

        Node.__update()

    
    @classmethod
    def __update(Node):
        '''
        Updates the Node class next id and next coords
        '''

        Node.__next_node_id += 1

        if Node.__next_node_coords[2] < 1200:
            Node.__next_node_coords[0] += Node.node_width
            Node.__next_node_coords[2] += Node.node_width
        elif Node.__next_node_coords[2] >= 1200 and Node.__next_node_coords[3] < 460:
            Node.__next_node_coords[0] = 2
            Node.__next_node_coords[2] = 22
            Node.__next_node_coords[1] += Node.node_height
            Node.__next_node_coords[3] += Node.node_height
        else:
            pass



    def draw(self, canvas: tk.Canvas):
        '''
        Draws the rectangle on a tk Canvas
        :param canvas: tk.Canvas object
        '''
        canvas.create_rectangle(*self.node_coords, fill=self.default_color, outline=self.outline_color, activefill=self.hover_color)



if __name__ == '__main__':
    app = App()
    app.run_app()
    print(type(Node()))
    print(app.to_string())