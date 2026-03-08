import pygame
import os
import random

class Zombie:
    def __init__(self, image_folder, spawn_edge="top"):
        self.images = [pygame.image.load(os.path.join(image_folder, f"zombie_frame_{i}.png")) for i in range(2)]
        self.image_index = 0
        self.image = self.images[0]  # ตั้งค่า image เริ่มต้น
        self.rect = self.image.get_rect()  # สร้าง rect จากขนาดของภาพ
        self.spawn_edge = spawn_edge  # ระบุว่าซอมบี้จะโผล่มาจากขอบใด
        self.reset_position()  # กำหนดตำแหน่งและความเร็วเริ่มต้น

    def update_animation(self):
        self.image_index = (self.image_index + 0.1) % len(self.images)
        self.image = self.images[int(self.image_index)]

    def reset_position(self):
        # กำหนดตำแหน่งเริ่มต้นให้ซอมบี้โผล่มาที่กึ่งกลางขอบหน้าจอ
        if self.spawn_edge == "top":
            self.rect.x = 400 - self.rect.width // 2  # กึ่งกลางด้านบน
            self.rect.y = -self.rect.height  # โผล่มาจากขอบบน
            self.speed_x = 0
            self.speed_y = random.randint(5, 10)

        elif self.spawn_edge == "side":
            side = random.choice(['left', 'right'])

            if side == 'left':
                self.rect.x = -self.rect.width  # กึ่งกลางด้านซ้าย
                self.rect.y = 300 - self.rect.height // 2
                self.speed_x = random.randint(5, 10)
            else:
                self.rect.x = 800  # กึ่งกลางด้านขวา
                self.rect.y = 300 - self.rect.height // 2
                self.speed_x = -random.randint(5, 10)

            self.speed_y = 0

    def move(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        # รีเซ็ตตำแหน่งเมื่อซอมบี้ออกจากจอ
        if self.rect.right < 0 or self.rect.left > 800 or self.rect.bottom < 0 or self.rect.top > 600:
            self.reset_position()

    def draw(self, screen):
        screen.blit(self.image, self.rect)
