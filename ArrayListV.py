import pygame

class ArrayListV:
    
    
    WHITE = (255, 255, 255)
    SCREEN_SIZE = (800,600)

    def __init__(self):
        pygame.init()
        
        
    def show(self):
        screen = pygame.display.set_mode(self.SCREEN_SIZE)
        screen.fill(self.WHITE)
        pygame.display.update()
        running = True
        while running:
            for event in pygame.event.get():
                print(event)
                if event.type == pygame.QUIT:
                    running = False
        pygame.quit()




    
