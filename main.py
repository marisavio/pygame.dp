from boto import set_file_logger
import pygame 
import random 
from audioop import cross
from turtle import width
from classes import dardo

class dardo(pygame.sprite.Sprite):
    def __init__(self, picture):
        pygame.sprite.Sprite.__init__(self)

        self.image = picture
        self.rect = self.image.get_rect()

        #som
    def update(self):
        self.rect.center = pygame.mouse.get_pos()
    
    def tiro(self):
        #iniciando som

        pygame.sprite.spritecollide(meumouse, alvogroup, True)

        while len(alvogroup) == 1:
            alvo = target(alvo_img)
            if pygame.sprite.spritecollideany(alvo,alvogroup) == None:
                alvogroup.add(alvo)

class target(pygame.sprite.Sprite):
    def __init__(self, picture):
        pygame.sprite.Sprite.__init__(self)

        self.image = picture 
        self.rect = self.image.get_rect()
        self.rect.center = [random.randrange(tamanho_alvo/2,WIDTH-tamanho_alvo/2),random.randrange(tamanho_alvo/2,WIDTH-tamanho_alvo/2)]


pygame.init()
pygame.mixer.init()

pygame.mouse.set_visible(False)

clock = pygame.time.Clock()
FPS = 100

WIDTH = 1100
HEIGHT = 750

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
        
    window.blit(imagem_de_fundo,(0,0))
    dardogroup.update()
    alvogroup.draw(window)
    dardogroup.draw(window)
        
    pygame.display.update()
    
