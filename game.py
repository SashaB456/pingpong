import pygame
pygame.init()
clock = pygame.time.Clock()
width = 1300
FPS = 60
height = 700
pygame.display.set_caption("Автор Гри Пінг-Понг: Білоус Олександр")
w = pygame.display.set_mode((width, height))
w.fill((230, 230, 250))
class GameSprite(pygame.sprite.Sprite):
    def __init__(self, a, b, image, x, y, speed, size):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(image), (a, b))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
        self.size = size
    def reset(self):
        w.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def update_r(self):
        ...
    def update_l(self):
        ...
ball = GameSprite(50, 50, 'ball.png', 100, 100, 6, (50, 50))
racket = GameSprite(160, 320, 'racket.png', 300, 100, 6, (160, 320))
game_over = False
finish = False
while not game_over:
    ball.reset()
    racket.reset()
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            game_over = True
    clock.tick(FPS)
    pygame.display.update()