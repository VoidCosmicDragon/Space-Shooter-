import pygame
import random
import time

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

# Class untuk peluru
class Bullet:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 5
        self.height = 10
        self.speed = 7

    def move(self):
        self.y -= self.speed

    def draw(self):
        pygame.draw.rect(screen, WHITE, (self.x, self.y, self.width, self.height))

# Inisialisasi objek
player = Player()
enemies = [Enemy()]
bullets = []

# Waktu terakhir menembak
last_shot = time.time()

# Loop utama
running = True
while running:
    pygame.time.delay(30)  # Delay untuk mengontrol kecepatan game
    screen.fill(BLACK)

    # Cek event (misalnya tombol keluar)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Cek input keyboard
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.move("left")
    if keys[pygame.K_RIGHT]:
        player.move("right")

    # Tembakan otomatis setiap 0.5 detik
    if time.time() - last_shot > 0.5:
        bullets.append(Bullet(player.x + player.width // 2, player.y))
        last_shot = time.time()

    # Update dan gambar semua peluru
    for bullet in bullets:
        bullet.move()
        bullet.draw()

    # Cek tabrakan antara peluru dan musuh
    for bullet in bullets[:]:
        for enemy in enemies[:]:
            if (enemy.x < bullet.x < enemy.x + enemy.width) and (enemy.y < bullet.y < enemy.y + enemy.height):
                enemies.remove(enemy)  # Musuh hilang jika kena peluru
                bullets.remove(bullet)  # Peluru juga hilang

    # Update dan gambar musuh
    for enemy in enemies:
        enemy.draw()

    player.draw()
    pygame.display.update()

pygame.quit()
