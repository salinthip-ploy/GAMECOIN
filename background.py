import pygame

class Background:
    def __init__(self, image_file, screen_size=(800, 600)):
        # โหลดภาพพื้นหลังโดยใช้ Pygame
        self.image = pygame.image.load(image_file)
        self.screen_width, self.screen_height = screen_size
        # ขนาดของภาพพื้นหลัง
        self.bg_width, self.bg_height = self.image.get_size()
        
        # ตั้งตำแหน่งเริ่มต้นของพื้นหลังให้เป็นจุดกึ่งกลางของภาพ
        self.position = [
            -(self.bg_width // 2 - self.screen_width // 2),
            -(self.bg_height // 2 - self.screen_height // 2)
        ]

    def update_position(self, player_position):
        # คำนวณตำแหน่งของพื้นหลังเพื่อเลื่อนไปตามตำแหน่งของตัวละคร
        self.position[0] = max(min(-player_position[0] + self.screen_width // 2, 0), -(self.bg_width - self.screen_width))
        self.position[1] = max(min(-player_position[1] + self.screen_height // 2, 0), -(self.bg_height - self.screen_height))
        
    def draw(self, screen):
        # วาดพื้นหลังในตำแหน่งที่คำนวณไว้
        screen.blit(self.image, self.position)
