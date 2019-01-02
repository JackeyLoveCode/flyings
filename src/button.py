import pygame,sys


class Button(object):
    def __init__(self, upimage, downimage, position):
        self.image_up = pygame.image.load(upimage).convert_alpha()
        self.image_down = pygame.image.load(downimage).convert_alpha()
        self.position = position
        self.button_out = True

    def is_over(self):
        point_x, point_y = pygame.mouse.get_pos()
        x, y = self.position
        w, h = self.image_up.get_size()
        x -= w / 2
        y -= h / 2
        in_x = x < point_x < x + w
        in_y = y < point_y < y + h
        return in_x and in_y

    def render(self, surface):
        x, y = self.position
        w, h = self.image_up.get_size()
        x -= w / 2
        y -= h / 2
        if self.is_over():
            surface.blit(self.image_down, (x, y))
            if self.button_out == True:
                buttonmusic.play()
                self.button_out = False
        else:
            surface.blit(self.image_up, (x, y))
            self.button_out = True
