import pygame 
import random
import time
import copy

# INITIALIZE PYGAME
pygame.init()


# GROUPS 
dinamitegroup = pygame.sprite.Group()

# CREATE A DISPLAY SURVACE AND SET ITS CAPTIONS
WINDOW_WIDTH = 945
WINDOW_HEIGHT = 600
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('DECO JOGO')

# CLASSES
class Jogo():
    lives = 0
    score = 0
    vermelho = False
    contador_vermelho = 0

class Mouse(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.rect = pygame.Rect(x,y,1,1)
        print(self.rect)

class Dardo(pygame.sprite.Sprite):
    def __init__(self, picture):
        pygame.sprite.Sprite.__init__(self)
        self.image = picture
        self.rect = self.image.get_rect()
<<<<<<< HEAD
    def update(self):
        self.rect.center = pygame.mouse.get_pos()

=======

        self.gunshot = pygame.mixer.Sound('snd/gun-gunshot.wav')

    def update(self):
        self.rect.center = pygame.mouse.get_pos()

    def tiro(self):
        self.gunshot.play()
>>>>>>> 5b526e328222770ee686f5f781beadb21e90bcda

class Target(pygame.sprite.Sprite):
    def __init__(self, picture):
        pygame.sprite.Sprite.__init__(self)
        self.image = picture
        self.rect = self.image.get_rect()
        self.rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2)
        self.target_starting_velocity = 3
        self.target_acceleration = .5
        self.target_velocity = self.target_starting_velocity
        self.target_dx = random.choice([-1, 1])
        self.target_dy = random.choice([-1, 1])

    def update(self):
        self.rect.x += self.target_dx*self.target_velocity
        self.rect.y += self.target_dy*self.target_velocity
        if self.rect.left <= 0 or self.rect.right >= WINDOW_WIDTH:
            self.target_dx = -1 * self.target_dx
        if self.rect.top <= 0 or self.rect.bottom >= WINDOW_HEIGHT:
            self.target_dy = -1 * self.target_dy

    def acertou(self):
        self.target_velocity += self.target_acceleration
        print('acertou')
        self.antigo_dx = self.target_dx
        self.antigo_dy = self.target_dy
        while (self.antigo_dx == self.target_dx and self.antigo_dy == self.target_dy):
            self.target_dx = random.choice([-1, 1])
            self.target_dy = random.choice([-1, 1])


class Dinamite(pygame.sprite.Sprite):
    def __init__(self, picture):
        pygame.sprite.Sprite.__init__(self)
        self.t1 = time.time()
        self.image = picture.copy()
        tamanho = 55
        x = random.randrange(int(tamanho/2) + 100,int(WINDOW_WIDTH-tamanho/2) - 100)
        y = random.randrange(int(tamanho/2) + 100,int(WINDOW_HEIGHT-tamanho/2) - 100)
        self.image = pygame.transform.scale(self.image, (tamanho, tamanho))
        self.rect = self.image.get_rect()
        print([x,y])
        print(self.rect)
        self.rect.center = [x,y]
        self.ativo = True
    def update(self):
        t2 = time.time()
<<<<<<< HEAD
        if t2 - t1 > 1.65:
            if self in dinamitegroup:
                self.ativo = False
                dinamitegroup.remove(self)
        else:
            if self.ativo:
                if pygame.sprite.spritecollideany(target, dinamitegroup) != None:
                    dinamitegroup.remove(self)
                    self.ativo = False
                    Jogo.lives -= 1
                    Jogo.vermelho = True
                    Jogo.contador_vermelho = 25
=======
        if t2 - t1 > 1.5:
            if self in alvogroup:
                alvogroup.remove(self)
                Jogo.pontos -= 25
                
                print(Jogo.pontos)
        
>>>>>>> 5b526e328222770ee686f5f781beadb21e90bcda


# SET BACKGROUND
background = pygame.image.load("TARGET PRACTICE/background.jpg")
background_rect = background.get_rect()
background = pygame.transform.scale(background, (945, 600))
background_rect.topleft = (0,0)

# LOAD IMAGES
target_image = pygame.image.load("TARGET PRACTICE/target.png")
target_image = pygame.transform.scale(target_image, (80, 80))
target_rect = target_image.get_rect()
target_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2)
target = Target(target_image)

cross_hair_image = pygame.image.load("TARGET PRACTICE/crosshair_outline_large.png")
cross_hair_image = pygame.transform.scale(cross_hair_image, (50, 50))
cross_hair = Dardo(cross_hair_image)
pygame.mouse.set_visible(False)

dinamite_image = pygame.image.load("TARGET PRACTICE/dynamite (3).png")





# FPS AND CLOCK
FPS = 60
clock = pygame.time.Clock()

# SET LIFES
starting_lives = 3
Jogo.score = 0
Jogo.lives = starting_lives


# COLOURS 
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# FONTS
font = pygame.font.Font("TARGET PRACTICE/galaxia.otf", 37)
font2 = pygame.font.Font("TARGET PRACTICE/galaxia.otf", 100)
font3 = pygame.font.Font("TARGET PRACTICE/galaxia.otf", 50)
font4 = pygame.font.Font("TARGET PRACTICE/galaxia.otf", 110)
font5 = pygame.font.Font("TARGET PRACTICE/galaxia.otf", 60)

titulo = font3.render("TARGET MADNESS", True, WHITE)
titulo_rect = titulo.get_rect()
titulo_rect.topleft = (50, 10)

score_text = font.render("SCORE: " + str(Jogo.score), True, WHITE)
score_rect = score_text.get_rect()
score_rect.topright = (WINDOW_WIDTH - 50, 10)


lives_text = font.render("LIVES: " + str(Jogo.lives), True, WHITE)
lives_rect = lives_text.get_rect()
lives_rect.topright = (WINDOW_WIDTH - 50, 50)


gameover = font2.render("GAMEOVER:", True, WHITE)
gameover_rect = gameover.get_rect()
gameover_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2)

continue_text = font.render("aperte 'ESPACO' para jogar novamente", True, WHITE)
continue_rect = continue_text.get_rect()
continue_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2 + 64)


INICIO_text = font4.render("TARGET MADNESS", True, WHITE)
INICIO_rect = INICIO_text.get_rect()
INICIO_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2)

INICIO_text2 = font5.render("APERTE 'ESPACO' PARA COMECAR", True, WHITE)
INICIO_rect2 = INICIO_text2.get_rect()
INICIO_rect2.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2 + 80)

# PERDEU VIDA TEXTO
perdeu_texto = font.render("ERROU", True, WHITE)
perdeu_rect = score_text.get_rect()

# ACERTOU TEXTO
acertou_texto = font.render("BANG", True, WHITE)
acertou_rect = score_text.get_rect()

assets = {}
assets["score_font"] = pygame.font.Font('font/PressStart2P.ttf', 28)

t1 = time.time()
tempo_limite = 2
exibir = False
ponto = False
contador = 45
ponto_verde = False
contador_verde = 25
ponto_vermelho = False
contador_vermelho = 25

# GAME LOOP
running = True 
estado = 'INICIO'
while running:
    if estado == 'INICIO':
        display_surface.blit(background, background_rect)
        display_surface.blit(INICIO_text, INICIO_rect)
        display_surface.blit(INICIO_text2, INICIO_rect2)




        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE]:
                estado = 'JOGANDO'
    else:
        # LOOP THROUGH A LIST OF EVENT OBJECTS THAT HAVE HAPPENED 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            keys = pygame.key.get_pressed()
            if keys[pygame.K_v]:
                Jogo.lives += 100


            t2 = time.time()
            if t2 - t1 > tempo_limite:
                tempo_limite *= 0.99
                t1 = t2
                dinamite = Dinamite(dinamite_image)
                colisao = pygame.sprite.spritecollide(target, dinamitegroup, dokill=True)
                if colisao == []:
                    dinamitegroup.add(dinamite)

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x = event.pos[0]
                mouse_y = event.pos[1]
                mouse_sprite = Mouse(mouse_x,mouse_y)
                if pygame.sprite.collide_rect(target,mouse_sprite):
                    target.acertou()
                    Jogo.lives += 1
                    Jogo.score += 1
                    contador_verde = 25
                    ponto_verde = True

                else:
                    Jogo.lives -= 1
                    contador = 45
                    exibir = True
                    Jogo.vermelho = True
                    Jogo.contador_vermelho = 25
                    perdeu_rect.center = (mouse_x + 18, mouse_y - 30)



        score_text = font.render("SCORE: " + str(Jogo.score), True, WHITE)
        lives_text = font.render("LIVES: " + str(Jogo.lives), True, WHITE)


        if Jogo.lives < 0:
            dinamitegroup = pygame.sprite.Group()
            display_surface.blit(gameover, gameover_rect)
            display_surface.blit(continue_text, continue_rect)
            pygame.display.update()
            paused = True 
            while paused:
                exibir = False
                for event in pygame.event.get():
                    keys = pygame.key.get_pressed()
                    if keys[pygame.K_SPACE]:
                        Jogo.score = 0
                        Jogo.lives = starting_lives
                        target = Target(target_image)
                        paused = False
                    if event.type == pygame.QUIT:
                        paused = False
                        running = False

        # UPDATE DISPLAY
        display_surface.blit(background, background_rect)
        display_surface.blit(titulo, titulo_rect)
        display_surface.blit(score_text, score_rect)
        display_surface.blit(lives_text, lives_rect)
        if exibir:
            contador -= 1
            if contador < 45:
                pygame.draw.circle(display_surface, (75, 48, 19), (mouse_x, mouse_y), 10, 0)
            if contador < 5:
                pygame.draw.circle(display_surface, (99, 62, 35), (mouse_x, mouse_y), 10, 0)
            if contador < 2:
                pygame.draw.circle(display_surface, (116, 74, 24), (mouse_x, mouse_y), 10, 0)
            if contador <= 0:
                exibir = False


        if ponto_verde:
            contador_verde -= 1
            lives_text = font.render("LIVES: " + str(Jogo.lives), True, (0, 255, 0))
            display_surface.blit(lives_text, lives_rect)
            lives_rect.topright = (WINDOW_WIDTH - 50, 50)
            if contador_verde < 0:
                ponto_verde = False


        if Jogo.vermelho:
            Jogo.contador_vermelho -= 1
            lives_text = font.render("LIVES: " + str(Jogo.lives), True, (255, 0, 0))
            display_surface.blit(lives_text, lives_rect)
            lives_rect.topright = (WINDOW_WIDTH - 50, 50)
            if Jogo.contador_vermelho < 0:
                Jogo.vermelho = False

            # display_surface.blit(perdeu_texto, perdeu_rect)
            if contador < 0:
                exibir = False
        display_surface.blit(target_image, target.rect)


        dinamitegroup.update()
        dinamitegroup.draw(display_surface)
        cross_hair.update()
        target.update()
        display_surface.blit(cross_hair_image, cross_hair.rect)
        pygame.display.update()


        # CLOCK
    pygame.display.update()
    clock.tick(FPS)

<<<<<<< HEAD
# END OF THE GAME
pygame.quit()
=======
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
>>>>>>> 5b526e328222770ee686f5f781beadb21e90bcda
