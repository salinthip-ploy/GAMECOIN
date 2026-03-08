import pygame
import random

class Coin:
    def __init__(self, image_path):
        self.image = pygame.transform.scale(pygame.image.load(image_path), (50, 50))
        self.rect = self.image.get_rect()
        self.reset_position()

    def reset_position(self):
        self.rect.x = random.randint(400, 770)
        self.rect.y = random.randint(0, 570)

    def draw(self, screen):
        screen.blit(self.image, self.rect)
