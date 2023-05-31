import pygame

pygame.init()


class Player(pygame.sprite.Sprite):

    negro = (0, 0, 0)

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.x = 100
        self.y = 500

    def handle_keys(self):
        key = pygame.key.get_pressed()
        if (key[pygame.K_a] == True or key[pygame.K_LEFT] == True) and self.x >= -75:
            self.x -= 0.75
        if (key[pygame.K_d] == True or key[pygame.K_RIGHT] == True) and self.x <= 300:
            self.x += 0.75

    def draw(self, surface, image):
        surface.blit(image, (self.x, self.y))
