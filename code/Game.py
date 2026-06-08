from code.Const import WIND_WIDHT, WIND_HEIGHT
from code.Menu import Menu

import pygame

class Game:

    def __init__(self): #construtor
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIND_WIDHT, WIND_HEIGHT))


    def run(self):


        while True:
            menu = Menu(self.window)
            menu.run()
            pass

