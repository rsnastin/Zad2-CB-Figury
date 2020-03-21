import pygame
from math import pi
import math
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

class Trojkat(Figury):
    def __init__(self, bok):
        Figury.__init__(self)
        self.bok = bok
        self.draw_method = pygame.draw.polygon
        self.draw_parameters = (self.color_red, [[2*self.bok, self.bok], [self.bok, 3*self.bok], [3*self.bok, 3*self.bok]], 0)
        self.oblicz_obwod()
        self.oblicz_pole()

    def oblicz_pole(self):
        self.pole = (self.bok*math.sqrt(3))/4

    def oblicz_obwod(self):
        self.obwod = 3 * self.bok

class Kwadrat(Figury):
    def __init__(self, bok):
        Figury.__init__(self)
        self.bok = bok
        self.draw_method = pygame.draw.rect
        self.draw_parameters = (self.color_red, [self.bok, self.bok, 2*self.bok, 2*self.bok])
        self.oblicz_obwod()
        self.oblicz_pole()

    def oblicz_pole(self):
        self.pole = self.bok*self.bok

    def oblicz_obwod(self):
        self.obwod = self.bok*4
class Prosotkat(Figury):
    def __init__(self, bok):
        Figury.__init__(self)
        self.bok = bok
        self.draw_method = pygame.draw.rect
        self.draw_parameters = (self.color_red, [self.bok, self.bok, self.bok*2, self.bok])
        self.oblicz_obwod()
        self.oblicz_pole()
    def oblicz_pole(self):
        self.pole = self.bok*(self.bok*2)

    def oblicz_obwod(self):
        self.obwod = self.bok*2+(self.bok*2)*2

menu = int(input("Witaj w programie\n1.Kolo\n2.Trojkat\n3.Kwadrat\n4.Prostokat\nWybor:"))
if menu == 1:
    a = Kolo(100)
    print(a.pole)
    print(a.obwod)
    a.draw_figure()
elif menu == 2:
    a = Trojkat(100)
    print(a.pole)
    print(a.obwod)
    a.draw_figure()
elif menu == 3:
    a = Kwadrat(100)
    print(a.pole)
    print(a.obwod)
    a.draw_figure()
elif menu == 4:
    a = Prosotkat(100)
    print(a.pole)
    print(a.obwod)
    a.draw_figure()
