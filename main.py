import pygame
import random

# Inisialisasi Pygame
pygame.init()

# Set ukuran layar
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Shooter (Tanpa Gambar)")

# Warna
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Class untuk pesawat
class Player:
    def __init__(self):
        self.x = WIDTH // 2
        self.y = HEIGHT - 50
        self.width = 50
        self.height = 30
        self.speed = 5
        self.hp = 500

    def move(self, direction):
        if direction == "left" and self.x > 0:
            self.x -= self.speed
        if direction == "right" and self.x < WIDTH - self.width:
            self.x += self.speed

    def draw(self):
        pygame.draw.rect(screen, GREEN, (self.x, self.y, self.width, self.height))

# Class untuk musuh
class Enemy:
    def __init__(self):
        self.x = random.randint(50, WIDTH - 50)
        self.y = random.randint(50, 150)
        self.width = 50
        self.height = 30
        self.hp = 100

    def draw(self):
        pygame.draw.rect(screen, RED, (self.x, self.y, self.width, self.height))

# Inisialisasi objek
player = Player()
enemies = [Enemy()]

# Loop utama
running = True
while running:
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.move("left")
    if keys[pygame.K_RIGHT]:
        player.move("right")

    player.draw()
    for enemy in enemies:
        enemy.draw()

    pygame.display.update()

pygame.quit()
