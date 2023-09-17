import pygame
pygame.init()
clock = pygame.time.Clock()
width = 1300
FPS = 60
height = 700
font_stat = pygame.font.Font(None, 25)
score1 = 0
score2 = 0
a = False
b = False
pygame.display.set_caption("Автор Гри Пінг-Понг: Білоус Олександр")
w = pygame.display.set_mode((width, height))
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
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_UP] and racket2.rect.y >= 0:
            racket2.rect.y -= 25
        elif keys_pressed[pygame.K_DOWN] and racket2.rect.y < height-320:
            racket2.rect.y += 25
    def update_l(self):
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_w] and racket1.rect.y >= 0:
            racket1.rect.y -= 25
        elif keys_pressed[pygame.K_s] and racket1.rect.y < height-320:
            racket1.rect.y += 25
ball = GameSprite(50, 50, 'ball.png', width/2, height/2, 0, (50, 50))
racket1 = Player(160, 320, 'racket.png', 10, 350-160, 7, (160, 320))
racket2 = Player(160, 320, 'racket.png', width-10-160, 350-160, 7, (160, 320))
bg_col = (99, 185, 80)
speed_x = 5
Test = True
speed_y = 5
x = False
score1_text = font_stat.render(str(score1), True, (255, 255, 255))
score2_text = font_stat.render(str(score2), True, (255, 255, 255))
game_over = False
finish = False
while not finish:
    if not game_over and x is True:
        win1_text = font_stat.render('Ліва сторона перемогла праву! Натисність на r щоб гра запустилася знову.', True, (255, 255, 255))
        win2_text = font_stat.render('Права сторона перемогла ліву! Натисність на r щоб гра запустилася знову.', True, (255, 255, 255))
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                pygame.quit()
                game_over = True
        if a is True:
            w.blit(win1_text, (width/2-50, height/2-50))
        elif b is True:
            w.blit(win2_text, (width/2-50, height/2-50))
        c = pygame.key.get_pressed()
        if c[pygame.K_r]:
            score1 = 0
            score2 = 0
            w.fill(bg_col)
            x = False
        clock.tick(FPS)
        pygame.display.update()
    elif not game_over and x is False:
        score1_text = font_stat.render(str(score1), True, (255, 255, 255))
        score2_text = font_stat.render(str(score2), True, (255, 255, 255))
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                pygame.quit()
                game_over = True
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        if ball.rect.y >= height-50 or ball.rect.y <= 0:
            speed_y *= -1
        elif ball.rect.colliderect(racket2.rect) or ball.rect.colliderect(racket1.rect) and Test == True:
            speed_x *= -1
            Test = False
        elif ball.rect.x == width/2:
            Test = True
        elif ball.rect.x >= width:
            score1 += 1
            ball.rect.x = width/2
            ball.rect.y = height/2
        elif ball.rect.x <= 0:
            score2 += 1
            ball.rect.x = width/2
            ball.rect.y = height/2
        elif score1 >= 5:
            x = True
            a = True
        elif score2 >= 5:
            x = True
            b = True
        w.fill(bg_col)
        ball.reset()
        racket1.reset()
        racket2.reset()
        racket1.update_l()
        racket2.update_r()
        w.blit(score1_text, (300, 100))
        w.blit(score2_text, (width-300, 100))
        clock.tick(FPS)
        pygame.display.update()