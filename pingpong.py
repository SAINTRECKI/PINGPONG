from pygame import *
from random import randint
win_width = 700
win_height = 500
img_ball = 'ball.png'
img_player = 'player.jpg'
img_back = 'background.jpg'
speed_x = 5
speed_y = 5
score_pl1 = 0
score_pl2 = 0

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__(player_image, player_x, player_y, size_x, size_y, player_speed)
    def update(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 0:
            self.rect.y-=self.speed
        if keys[K_s] and self.rect.y < win_height - 130:
            self.rect.y+=self.speed
    def update1(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 0:
            self.rect.y-=self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 130:
            self.rect.y+=self.speed
class Ball(GameSprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__(player_image, player_x, player_y, size_x, size_y, player_speed)
    def update(self):
        global speed_x; global speed_y
        if self.rect.y <= 0 or self.rect.y >= win_height - 50:
            speed_y = -speed_y
        self.rect.x += speed_x
        self.rect.y += speed_y
            
            
        
player1 = Player(img_player, 20, win_height - 300, 15, 130, 5)
player2 = Player(img_player, win_width-30, win_height - 300, 15, 130, 5)
players = sprite.Group()
ball = Ball(img_ball, 100, win_height-140, 70, 70, 0)
balls = sprite.Group()
balls.add(ball)
players.add(player1); players.add(player2)
window = display.set_mode((win_width, win_height))
display.set_caption("PING PONG")
background = transform.scale(image.load(img_back), (win_width, win_height))
game = True
finish = False
clock = time.Clock()
FPS = 60
font.init()
font2 = font.SysFont("Arial",36)
font3 = font.SysFont("Arial", 60)
win_pl1 = font3.render("Выиграл 1 игрок!", 1, (255, 0, 0))
win_pl2 = font3.render("Выиграл 2 игрок!", 1, (255, 0, 0))
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if not finish:
        window.blit(background, (0, 0))
        score = font2.render(str(score_pl1) + " : " + str(score_pl2), 1, (255, 255, 255))
        if sprite.groupcollide(players, balls, False, False):
            speed_x = -speed_x
        if ball.rect.x > win_width:
            score_pl1 += 1
            ball.rect.x = 600; ball.rect.y = randint(30, win_height - 140)
            speed_x = -speed_x
        elif ball.rect.x < 0:
            score_pl2 += 1
            ball.rect.x = 100; ball.rect.y = randint(30, win_height - 140)
            speed_x = -speed_x
        player1.update()
        player1.reset()
        player2.update1()
        player2.reset()
        ball.update()
        ball.reset()
        window.blit(score, (321, 10))


    display.update()
    clock.tick(FPS)




