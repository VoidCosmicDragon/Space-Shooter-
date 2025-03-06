import pygame
import random
import time

# Inisialisasi Pygame
pygame.init()

# Set ukuran layar
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Shooter")

# Warna
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Font untuk skor dan HP
font = pygame.font.Font(None, 36)

# Class untuk pesawat
class Player:
    def __init__(self):
        self.x = WIDTH // 2
        self.y = HEIGHT - 60
        self.width = 50
        self.height = 30
        self.speed = 7
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
        self.speed = 2

    def move(self):
        self.y += self.speed  # Musuh turun ke bawah

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
score = 0  # Skor pemain
last_shot = time.time()  # Waktu terakhir menembak

# Loop utama
running = True
while running:
    pygame.time.delay(30)  # Delay untuk mengontrol kecepatan game
    screen.fill(BLACK)

    # Cek event (misalnya tombol keluar)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Cek input keyboard untuk gerakan pesawat
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.move("left")
    if keys[pygame.K_RIGHT]:
        player.move("right")

    # Tembakan otomatis setiap 0.5 detik
    if time.time() - last_shot > 0.5:
        bullets.append(Bullet(player.x + player.width // 2, player.y))
        last_shot = time.time()

    # Update & gambar semua peluru
    for bullet in bullets[:]:
        bullet.move()
        bullet.draw()

    # Update & gambar musuh
    for enemy in enemies[:]:
        enemy.move()
        enemy.draw()

        # Jika musuh menyentuh pemain, kurangi HP pemain
        if enemy.y + enemy.height >= player.y and enemy.x in range(player.x, player.x + player.width):
            player.hp -= 20
            enemies.remove(enemy)  # Hapus musuh setelah menyerang

    # Cek tabrakan antara peluru dan musuh
    for bullet in bullets[:]:
        for enemy in enemies[:]:
            if (enemy.x < bullet.x < enemy.x + enemy.width) and (enemy.y < bullet.y < enemy.y + enemy.height):
                enemy.hp -= 50  # Setiap peluru mengurangi HP musuh
                bullets.remove(bullet)
                if enemy.hp <= 0:  # Jika HP musuh habis, hapus dan tambah skor
                    enemies.remove(enemy)
                    score += 100

    # Tambahkan musuh baru secara berkala
    if random.randint(1, 50) == 1:
        enemies.append(Enemy())

    # Gambar pesawat pemain
    player.draw()

    # Tampilkan skor dan HP
    score_text = font.render(f"Score: {score}", True, WHITE)
    hp_text = font.render(f"HP: {player.hp}", True, WHITE)
    screen.blit(score_text, (10, 10))
    screen.blit(hp_text, (10, 40))

    pygame.display.update()

pygame.quit()
