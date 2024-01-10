import pygame
import random

class Ball:
    def __init__(self):
        w, h = pygame.display.get_surface().get_size()
        self.radius = 10
        self.position = (w // 2, h // 2)
        self.velocity = [random.choice([-1, 1]), random.choice([-1, 1])]
        self.score_1 = 0
        self.score_2 = 0

    def draw(self):
        pygame.draw.circle(pygame.display.get_surface(), (255, 255, 255), self.position, self.radius)

    def update_position(self):
        x, y = self.position
        vx, vy = self.velocity
        self.position = (x + vx, y + vy)

    def check_collision(self, paddles):
        for paddle in paddles:
            px, py = paddle.position
            pw, ph = paddle.rect
            bx, by = self.position
            distance = ((px + pw / 2 - bx) ** 2 + (py + ph / 2 - by) ** 2) ** 0.5
            if distance < (self.radius + max(pw, ph)) / 2:
                self.velocity[0] *= -1

    def check_wall_collision(self, screen_size):
        w, h = screen_size
        bx, by = self.position

        if by - self.radius <= 0 or by + self.radius >= h:
            self.velocity[1] *= -1

        if bx - self.radius <= 0:
            self.score_2 += 1
            self.reset_position()
        elif bx + self.radius >= w:
            self.score_1 += 1
            self.reset_position()

    def reset_position(self):
        w, h = pygame.display.get_surface().get_size()
        self.position = (w // 2, h // 2)
        self.velocity = [random.choice([-1, 1]), random.choice([-1, 1])]
