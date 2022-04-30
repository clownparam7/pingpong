from pygame import *
from random import randint


 
font.init()
font2 = font.Font(None, 36)
 
# нам нужны такие картинки:
img_back = "back.png"
img_raketka = "raketka2.jpg"
img_ball = "ball3.png"
 
 

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        sprite.Sprite.__init__(self)
 
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
 
        # каждый спрайт должен хранить свойство rect - прямоугольник, в который он вписан
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
 
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
 
class Player(GameSprite):
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 100:
            self.rect.y += self.speed
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 100:
            self.rect.y += self.speed
            
win_width = 700
win_height = 500
display.set_caption("pingpong")
window = display.set_mode((win_width, win_height))
background = transform.scale(image.load(img_back), (win_width, win_height))
    


lol = Player(img_raketka, 5, win_height - 100, 80, 100, 20)
lol2 = Player(img_raketka, 620, win_height - 500, 80, 100, 20)
ball = GameSprite(img_ball, 325, 250,45, 45, 15)
clock = time.Clock()
finish = False
FPS = 60
run = True
while run:
    # событие нажатия на кнопку Закрыть
    for e in event.get():
        if e.type == QUIT:
            run = False
 
    if not finish:
        # обновляем фон
        window.blit(background,(0,0))
        direction = randint(1,2) 
        text_lose = font2.render("игрок 1 лох" , 1, (255, 0, 0))
        text_lose2 = font2.render("игрок 2 лох", 1, (0, 255, 0))
        lol.update_l()
        lol2.update_r()
 
        # обновляем их в новом местоположении при каждой итерации цикла
        lol.reset()
        lol2.reset()
        ball.reset()
        #monsters.draw(window)

        display.update()
    clock.tick(FPS)
