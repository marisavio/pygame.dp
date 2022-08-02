import pygame
import random

class dardo(pygame.sprite.Sprite):
    def __init__(self, picture):
        pygame.sprite.Sprite(self)

        self.image = picture
        self.rect = self.image.get_rect()

        #som
    
    def update(self):
        self.rect.center = pygame.mouse.get_pos()
    
    def tiro(self):
        #iniciando som
        pygame.sprite.spritecollide(meumouse, targetgroup, True)

        while len(alvogroup) != 1:
            alvo = target(target_img)
            if pygame.sprite.spritecollideany(alvo,targetgroup) == None:
                targetgroup.add(alvo)
        
#class alvo(pygame.sprite.Sprite):
#   def __init__