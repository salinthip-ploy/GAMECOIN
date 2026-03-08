import pygame
from player import Player
from coin import Coin
from zombie import Zombie
from background import Background
from score import Score

class Game:
    def __init__(self, screen, clock):
        self.screen = screen
        self.clock = clock
        self.background = Background("assets/background/bg.jpg")
        self.player = Player("assets/ghost")
        self.coin = Coin("assets/coin.png")
        self.zombie_top = Zombie("assets/zombie", spawn_edge="top")
        self.zombie_side = Zombie("assets/zombie", spawn_edge="side")
        self.font = pygame.font.Font(None, 36)
        self.coin_sound = pygame.mixer.Sound("assets/coin_sound.mp3")
        self.game_over = False
        self.score = Score()

    def draw_text(self, text, x, y, color):
        """ฟังก์ชันสำหรับวาดข้อความบนหน้าจอ"""
        text_surface = self.font.render(text, True, color)
        self.screen.blit(text_surface, (x, y))

    def check_collision(self):
        # ตรวจสอบการชนกันระหว่าง player กับ coin
        if self.player.rect.colliderect(self.coin.rect):
            self.player.collect_coin()
            self.coin.reset_position()
            self.coin_sound.play()

        # ตรวจสอบการชนกันระหว่าง player กับ zombie ทั้งสองตัว
        for zombie in [self.zombie_top, self.zombie_side]:
            if self.player.rect.colliderect(zombie.rect):
                distance_x = abs(self.player.rect.centerx - zombie.rect.centerx)
                distance_y = abs(self.player.rect.centery - zombie.rect.centery)
                if distance_x < self.player.rect.width * 0.5 and distance_y < self.player.rect.height * 0.5:
                    self.game_over = True
                    self.score.save_high_score(self.player.score)

    def run(self):
        running = True
        while running:
            self.screen.fill((0, 0, 0))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            keys = pygame.key.get_pressed()
            self.player.move(keys)
            self.player.update_animation()

            # อัปเดตการเคลื่อนไหวและการแสดงผลของซอมบี้ทั้งสองตัว
            for zombie in [self.zombie_top, self.zombie_side]:
                zombie.move()
                zombie.update_animation()
            self.check_collision()

            # อัปเดตตำแหน่งพื้นหลังให้เคลื่อนตามผู้เล่น
            self.background.update_position(self.player.rect.topleft)
            self.background.draw(self.screen)

            # วาดองค์ประกอบทั้งหมด
            self.player.draw(self.screen)
            self.coin.draw(self.screen)
            self.zombie_top.draw(self.screen)
            self.zombie_side.draw(self.screen)
            self.draw_text(f"Score: {self.player.score}", 10, 10, (255, 255, 255))
            self.draw_text(f"High Score: {self.score.high_score}", 10, 40, (255, 255, 255))

            if self.game_over:
                self.draw_text("Game Over", 350, 300, (255, 0, 0))
                pygame.display.flip()
                pygame.time.wait(2000)
                running = False

            pygame.display.flip()
            self.clock.tick(30)
