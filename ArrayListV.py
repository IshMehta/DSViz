# import pygame

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
        window.title("Array List Visualiser")


        main_frame = tk.Frame(window)
        main_frame.pack(fill=tk.BOTH, expand=True, side= tk.TOP)

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


        window.mainloop()

    def addNode(self, node):
        self.list.append(node)
                


