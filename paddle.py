import pygame

default_position = 50

class Paddle:
    def __init__(self, side: int):
        w, h = pygame.display.get_surface().get_size()
        self.w = w
        self.h = h
        self.rect = (10, 50)
        rw, rh = self.rect
        self.position = (default_position, default_position) if side == 0 else (w - (rw + default_position), h - (rh + default_position))

    def draw(self):
        pygame.draw.rect(pygame.display.get_surface(), (255, 255, 255), (self.position, self.rect))

    def update_position(self):
        x, y = self.position
        self.position = (x, y)

    def move_up(self):
        x, y = self.position
        if (y - 10) > 0:
            self.position = (x, y - 10)
            self.update_position()

    def move_down(self):
        x, y = self.position
        if ((y  + 10) + self.rect[1]) < self.h:
            self.position = (x, y + 10)
            self.update_position()
