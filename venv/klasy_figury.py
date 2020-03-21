import pygame
from math import pi

class Figury(object):
    def __init__(self):
        self.pole = 0
        self.obwod = 0
        self.draw_method = None
        self.draw_parameters = []
        self.init_screen()

    def oblicz_pole(self):
        pass

    def oblicz_obwod(self):
        pass

    def init_screen(self):
        pygame.init()
        self.color_white = (255, 255, 255)
        self.color_black = (0, 0, 0)
        self.color_red = (255, 0, 0)
        self.color_green = (0, 255, 0)
        self.color_blue = (0, 0, 255)

    def draw_figure(self):
        self.screen = pygame.display.set_mode((400, 400))
        self.screen.fill(self.color_black)
        self.draw_method(self.screen, *self.draw_parameters)
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            pygame.display.update(),

class Kolo(Figury):
    def __init__(self, r):
        Figury.__init__(self)
        self.r = r
        self.draw_method = pygame.draw.circle
        self.draw_parameters = [self.color_red, (200, 200), r, 0]
        self.oblicz_obwod()
        self.oblicz_pole()

    def oblicz_pole(self):
        self.pole = pi*self.r*self.r

    def oblicz_obwod(self):
        self.obwod = 2 * pi *self.r



a = Kolo(100)
print(a.pole)
print(a.obwod)
a.draw_figure()



