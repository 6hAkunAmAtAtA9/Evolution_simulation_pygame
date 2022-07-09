import pygame.font

class Button():

    def __init__(self, e_game, msg, coords1, coords2):

        self.screen = e_game.screen
        self.screen_rect = e_game.screen.get_rect()

        self.width, self.height = 100, 30
        self.button_color = (0, 255, 0)
        self.text_color = (0, 0, 0)
        self.font = pygame.font.SysFont(None, 16)

        self.rect = pygame.Rect(coords1, coords2, self.width, self.height)
        self.prep_msg(msg)

    def prep_msg(self, msg):
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_buttom(self):
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
