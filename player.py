import pygame
import os

class Player:
    def __init__(self, image_folder, scale_factor=0.2):
        original_images = [pygame.image.load(os.path.join(image_folder, f"ghost_frame_{i}.png")) for i in range(2)]
        self.images = [pygame.transform.scale(image, (int(image.get_width() * scale_factor), int(image.get_height() * scale_factor))) for image in original_images]
        self.image_index = 0
        self.rect = self.images[0].get_rect(center=(200, 300))
        self.speed = 5
        self.score = 0
        self.multiplier = 1

    def update_animation(self):
        self.image_index = (self.image_index + 0.1) % len(self.images)
        self.image = self.images[int(self.image_index)]

    def move(self, keys):
        if keys[pygame.K_UP] and self.rect.top > 0:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN] and self.rect.bottom < 600:
            self.rect.y += self.speed
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < 800:
            self.rect.x += self.speed

    def collect_coin(self):
        self.score += 1 * self.multiplier
        if self.score >= 20:
            self.multiplier = 2

    def draw(self, screen):
        screen.blit(self.image, self.rect)
