import pygame
import random
pygame.init()

W, H = 800, 600

fps = 60

white = (255, 255, 255)

screen = pygame.display.set_mode((W, H))

pygame.display.set_caption("flappy bird") 

font = pygame.font.SysFont("Bauhaus 93", 59)
Bg = pygame.image.load("image\Bg.png")
ground_img = pygame.image.load("image\ground.png")
restart = pygame.image.load("image\Restart.png")

#game variables

ground_scroll = 0
scroll_speed = 5
flying = False
Game_over = False
pipe_gap = 120
pipe_freq = 1500
last_pipe = pygame.time.get_ticks() - pipe_freq
score = 0
passed_pipe = False

#game functions

def draw_text(text, font, color, x, y):
    screen.blit(font.render(text, True, color,)(x, y))

def reset_game():
    pipe_group.empty()#remove the pipes
    flappy.rect.center = (110, H // 2)#bird pos
    global score, passed_pipe
    score = 0
    passed_pipe = False
    return score

class Bird(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.images = [pygame.image.load(" C:\Users\gaura\Documents\pygame one\\flappy bird\image\Bird{i}.png")for i in range(1,4)]
        self.index = 0
        self.counter = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect(center = (x, y))
        self.vel = 0
        self.clicked = False

        
    def update(self):
        pass

class Button():
    def __init__(self, x, y, img):
        pass
    def draw(self):
        pass

#grouping the sprites
bird_group = pygame.sprite.Group()
pipe_group = pygame.sprite.Group()

#objects of class Bird

flappy = Bird(100,H//2)
bird_group.add(flappy)
Restart_button = Button(W//2 - 50, H//2 - 80, restart)

Clock = pygame.time.Clock()
running = True

while running:
    Clock.tick(fps)
    screen.blit(Bg, (0, 0))
    if not Game_over and flying:
        time_now = pygame.time.get_ticks()

    

    #updating the bird
    bird_group.update()
    bird_group.draw(screen)
    pipe_group.draw(screen)
    draw_text(str(score), font, white, W // 2, 20)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and not flying and not Game_over:
            flying = True


    pygame.display.update()

pygame.quit()
