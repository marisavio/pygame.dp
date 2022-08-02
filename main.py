from boto import set_file_logger
import pygame 
import random 
from audioop import cross
from turtle import width
from classes import dardo
import time

class Jogo():
    pontos = 100

class dardo(pygame.sprite.Sprite):
    def __init__(self, picture):
        pygame.sprite.Sprite.__init__(self)

        self.image = picture
        self.rect = self.image.get_rect()

        self.gunshot = pygame.mixer.Sound('snd/gun-gunshot.wav')

    def update(self):
        self.rect.center = pygame.mouse.get_pos()

    def tiro(self):
        self.gunshot.play()

        pygame.sprite.spritecollide(meumouse, alvogroup, True)

        #while len(alvogroup) == 1:
            #alvo = target(alvo_img)
            #if pygame.sprite.spritecollideany(alvo,alvogroup) == None:
                #alvogroup.add(alvo)

class target(pygame.sprite.Sprite):
    def __init__(self, picture):
        pygame.sprite.Sprite.__init__(self)
        self.t1 = time.time()
        self.image = picture 
        self.rect = self.image.get_rect()
        x = random.randrange(tamanho_alvo/2,WIDTH-tamanho_alvo/2)
        y = random.randrange(tamanho_alvo/2,HEIGHT-tamanho_alvo/2)
        print([x,y])
        print(self.rect)
        self.rect.center = [x,y]
    def update(self):
        t2 = time.time()
        if t2 - t1 > 1.5:
            if self in alvogroup:
                alvogroup.remove(self)
                Jogo.pontos -= 25
                
                print(Jogo.pontos)
        

pygame.init()
pygame.mixer.init()

pygame.mouse.set_visible(False)

clock = pygame.time.Clock()
FPS = 100

WIDTH = 1000
HEIGHT = 600

window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Tiro ao alvo')

imagem_de_fundo = pygame.image.load('PNG/wood.png').convert_alpha()
imagem_de_fundo = pygame.transform.scale(imagem_de_fundo, (WIDTH, HEIGHT))

tamanho_alvo = 100 

alvo_img = pygame.image.load('PNG/target2.png').convert_alpha()
alvo_img = pygame.transform.scale(alvo_img, (tamanho_alvo, tamanho_alvo))

dardogroup = pygame.sprite.Group()
alvogroup = pygame.sprite.Group()

dardo_img = pygame.image.load('PNG/crosshair_outline_large.png').convert_alpha()

meumouse = dardo(dardo_img)
dardogroup.add(meumouse)

while len(alvogroup) != 1:
    alvo = target(alvo_img)
    if pygame.sprite.spritecollideany(alvo,dardogroup) == None:
        alvogroup.add(alvo)


assets = {}
assets["score_font"] = pygame.font.Font('font/PressStart2P.ttf', 28)

t1 = time.time()
tempo_limite = 3
#-------- TELA PRINCIPAL --------
game = True 
while game:
    clock.tick(FPS)

    # ----- Trata eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            meumouse.tiro()            
    t2 = time.time()
    if t2 - t1 > tempo_limite:
        tempo_limite *= 0.95
        t1 = t2
        alvo = target(alvo_img)
        if pygame.sprite.spritecollideany(alvo,dardogroup) == None:
            alvogroup.add(alvo)
    window.blit(imagem_de_fundo,(0,0))
    alvogroup.update()
    dardogroup.update()
    alvogroup.draw(window)
    dardogroup.draw(window)
    
    
    # SCORE
    if Jogo.pontos <= 0:
        
        game = False

    text_surface = assets['score_font'].render("{:08d}".format(Jogo.pontos), True, (255, 255, 255))
    text_rect = text_surface.get_rect()
    text_rect.midtop = (HEIGHT/2, 200)
    window.blit(text_surface, text_rect)

    pygame.display.update()