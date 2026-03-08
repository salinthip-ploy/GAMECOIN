import pygame
from game import Game

# ตั้งค่า pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Ghost Run Coin Collector")
clock = pygame.time.Clock()

# เริ่มเกม
if __name__ == "__main__":
    game = Game(screen, clock)
    game.run()
    pygame.quit()
