import pygame.image
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import WIND_WIDHT, MENU_OPTION, WIND_HEIGHT


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load("./assets/start_window/startWindow.png")
        self.rect = self.surf.get_rect(left = 0, top =0)


    def run(self, ):
        pygame.mixer_music.load("./assets/music/Fase1.mp3")
        pygame.mixer_music.play(-1)

        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(80, "The", (73, 157, 208), ((WIND_WIDHT / 2 + 30), 50))
            self.menu_text(80, "Knight", (73, 157, 208), ((WIND_WIDHT / 2 +180), 50))
            self.menu_text(40, "and the", (73, 157, 208), ((WIND_WIDHT / 2 + 100), 90))
            self.menu_text(40, "Cat", (253, 204, 13), ((WIND_WIDHT / 2 + 178), 90))

            for i in range(len(MENU_OPTION)):
                self.menu_text(40, MENU_OPTION[i], (253, 204, 13), (200, 200 + 60 * i))
            pygame.display.flip()
            #eventos na tela
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

    def menu_text(self , text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.Font("assets/font/Cardinal.ttf", text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center = text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)
