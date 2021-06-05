# import pygame

from DSViz.NoneError import NoneError
import tkinter as tk
from tkinter.constants import BOTTOM, HORIZONTAL

class ArrayListV:
    
    
    # WHITE = (255, 255, 255)
    # SCREEN_SIZE = (800,600)
    # list = []

    # def __init__(self):
    #     pygame.init()
        
        
    # def show(self):
    #     screen = pygame.display.set_mode(self.SCREEN_SIZE)
    #     screen.fill(self.WHITE)
    #     pygame.display.set_caption("Array List")
    #     pygame.display.update()
    #     pygame
    #     running = True
    #     while running:
    #         for event in pygame.event.get():
    #             # print(event)
    #             if event.type == pygame.QUIT:
    #                 running = False
    #     pygame.quit()

    # def addNode(self, node):
    #     self.list.append(node)


    list = []
    WIDTH = 800
    HEIGHT = 600

    def show(self):
        window = tk.Tk()
        window.geometry("1000x800")
        window.title("Array List Visualiser")


        main_frame = tk.Frame(window)
        main_frame.pack(fill=tk.BOTH, expand=True, side= tk.TOP)

        if len(self.list) != 0:
            label = tk.Label(master = main_frame, text="Array List looks like this: ")
            label.pack(side=tk.TOP)

            canvas = tk.Canvas(master=main_frame, width = 800, height = 600)
            canvas.pack( fill=tk.BOTH, expand=True)

            scrollbar = tk.Scrollbar(master = main_frame, orient=HORIZONTAL, command=canvas.xview)
            scrollbar.pack(side = BOTTOM, fill=tk.X)
            canvas.configure(xscrollcommand=scrollbar.set)
            canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

            secondFrame = tk.Frame(canvas)
            canvas.create_window((0,0), window = secondFrame, anchor="nw")



            for i in range(len(self.list)):
                subframe = tk.Frame(
                        master=secondFrame,
                        relief=tk.RAISED,
                        borderwidth=1
                    )
                subframe.grid(row=1, column=i, sticky='nsew')
                label = tk.Label(master=subframe, text=f"Index \n{i}")
                label.pack(fill=tk.BOTH)

            for j in range(len(self.list)):
                subframe = tk.Frame(
                    master=secondFrame,
                    relief=tk.RAISED,
                    borderwidth=1
                    
                )
                subframe.grid(row=2, column=j, sticky='nsew')
                label = tk.Label(master=subframe, text=self.list[j])
                label.pack(fill=tk.BOTH)
        else :
            label = tk.Label(master = main_frame, text = "Array List is empty.")
            label.pack(fill=tk.BOTH)
            # label.grid(row=1, column=1)

        window.mainloop()

    def addNode(self, node):
        if node is None:
            raise NoneError("Node in Array List cannot be None")

        if not isinstance(node, (str, float, int)):
            raise TypeError("Node in Array List has to be of type String, Integer or Float")
            
        self.list.append(node)
                


