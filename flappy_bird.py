#import modules and Functions
from sys import exit
import pygame
from random import randint

#Set Display Window or Size
pygame.init()
screen_width = 400
screen_heigt = 600
pygame.display.set_caption("Welcome To Flappy World", "Flappy Bird")
main_screen = pygame.display.set_mode((screen_width, screen_heigt))
pygame.display.set_icon(pygame.image.load("images/birds/bird01.png").convert_alpha())

#class for our Bird
class Bird:
    def __init__(self):
        self.bird1 = pygame.image.load("images/birds/bird01.png").convert_alpha()
        self.bird2 = pygame.image.load("images/birds/bird02.png").convert_alpha()
        self.bird3 = pygame.image.load("images/birds/bird03.png").convert_alpha()
        self.bird4 = pygame.image.load("images/birds/bird04.png").convert_alpha()
        self.bird = [self.bird1, self.bird2, self.bird3, self.bird4]
        self.rotatebird = None
        self.bird_rect = self.bird1.get_rect(center = (100, 200))
        self.gravity = 0.6
        self.velocity = 0

    def drawbird(self):
        if 20 < self.bird_rect.bottom < 460:
            self.velocity += self.gravity
            self.bird_rect.centery += self.velocity
        else:
            main.gameRun = False
        self.rotateBird = self.bird[i]
        self.rotateBird = pygame.transform.rotate(self.rotateBird, -self.velocity*2)
        main_screen.blit(self.rotateBird, self.bird_rect)

#class for our Pipe
class Pipe:
    def __init__(self):
        self.pipe = pygame.image.load("images/pipe.png").convert_alpha()
        self.pipe2 = pygame.transform.flip(self.pipe, False, True)
        self.rect1 = self.pipe.get_rect(topleft = [420, 300])
        self.rect2 = self.pipe.get_rect(topleft = [620, 350])
        self.rect3 = self.pipe.get_rect(topleft = [820, 390])
        self.rect4 = self.pipe2.get_rect(topleft = [420, -120])
        self.rect5 = self.pipe2.get_rect(topleft = [620, -70])
        self.rect6 = self.pipe2.get_rect(topleft = [820, -30])
        self.pipe_list = [[self.rect1, self.rect4], [self.rect2, self.rect5], [self.rect3, self.rect6]]
    def drawPipe(self):
        for item in self.pipe_list:
            main_screen.blit(self.pipe, item[0])
            main_screen.blit(self.pipe2, item[1])
            x = randint(350, 550)
            for index,item1 in enumerate(item):
                if item1.centerx == -20:
                    item1.centerx = 570
                    if index == 0:
                        item1.centery = x
                    else:
                        item1.centery = x-420

        self.movePipe()
    
    def movePipe(self):
        self.rect1.centerx -= 5
        self.rect3.centerx -= 5
        self.rect2.centerx -= 5
        self.rect4.centerx -= 5  
        self.rect5.centerx -= 5
        self.rect6.centerx -= 5 

#class for GameControl
class Main:
    def __init__(self):
        self.background = pygame.image.load("images/background.png").convert_alpha()
        self.ground = pygame.image.load("images/ground.png").convert_alpha()
        self.groundx = 0
        self.score = 0
        self.start = True
        self.gameRun = False

    def startScreen(self):
        font = pygame.font.SysFont("Cascadia Code", 45, True, True)
        font2 = pygame.font.SysFont("Cascadia Code", 35, True,)
        font.underline = True
        text = font.render("Flappy Bird By Asif", True, (255, 255, 255))
        text2 = font2.render("Press Enter or Click to Start", True, (255, 255, 255))
        text3 = font2.render("Use Down Arrow key to Fly", True, (100, 50, 0))
        main_screen.blit(self.background, [0, 0])
        main_screen.blit(self.ground, [0, 480])
        main_screen.blit(text, [(400-text.get_width())/2, 120])
        main_screen.blit(text2, [(400-text2.get_width())/2, 345])
        main_screen.blit(text3, [(400-text3.get_width())/2, 400])
        main_screen.blit(bird.bird[i], [100, 250])

    def gameOverScreen(self):
        pipe.rect1.topleft = [420, 300]
        pipe.rect2.topleft = [620, 350]
        pipe.rect3.topleft = [820, 390]
        pipe.rect4.topleft = [420, -120]
        pipe.rect5.topleft = [620, -70]
        pipe.rect6.topleft = [820, -30]
        pipe.pipe_list = [[pipe.rect1, pipe.rect4], [pipe.rect2, pipe.rect5], [pipe.rect3, pipe.rect6]]
        font1 = pygame.font.SysFont("Cascadia Code", 60, True, True)
        font1.underline = True
        font2 = pygame.font.SysFont("Cascadia Code", 38)
        font3 = pygame.font.SysFont("Cascadia Code", 50)
        text = font1.render("Game Over", True, (255, 0, 0))
        text2 = font2.render("Press Enter or Click to Restart", True, (255, 255, 255))
        text3 = font3.render(f"Your Score :- {self.score}", True, "white")
        main_screen.blit(self.background, [0, 0])
        main_screen.blit(self.ground, [0, 480])
        main_screen.blit(text, [(400-text.get_width())/2, 120])
        main_screen.blit(text2, [(400-text2.get_width())/2, 345])
        main_screen.blit(text3, [(400-text3.get_width())/2, 240])
        main_screen.blit(bird.rotateBird, bird.bird_rect)

    def backgroundRun(self):
        if self.groundx == -400:
            self.groundx = 0
        main_screen.blit(self.background, [0, 0])
        pipe.drawPipe()
        main_screen.blit(self.ground, [self.groundx+400, 480])
        main_screen.blit(self.ground, [self.groundx, 480])
        self.groundx -= 5

    def gameisrunning(self):
        if self.start:
            self.startScreen()
        elif not self.gameRun:
            self.gameOverScreen()
        else:
            self.backgroundRun()
            bird.drawbird()
            self.showScore()
            self.gameOver()

    def showScore(self):
        if pipe.pipe_list[0][0].left == 90:
            self.score += 1
        elif pipe.pipe_list[1][0].left == 90:
            self.score += 1
        elif pipe.pipe_list[2][0].left == 90:
            self.score += 1
        font1 = pygame.font.SysFont("Cascadia Code", 60, True, True)
        text = font1.render(f"{self.score}", True, (250, 200, 250))
        main_screen.blit(text, [150, 100])
    
    def gameOver(self):
        rect1 = bird.bird_rect
        rect2 = pipe.rect1
        rect3 = pipe.rect2
        rect4 = pipe.rect3
        rect5 = pipe.rect4
        rect6 = pipe.rect5
        rect7 = pipe.rect6
        if rect1.collidelist([rect2, rect3, rect4, rect5, rect6, rect7]) != -1:
            self.gameRun =False

#calling all Classes
main = Main()
bird = Bird()
pipe = Pipe()

#change Bird image at given time
changePic = pygame.USEREVENT
pygame.time.set_timer(changePic, 100)

#frames per Second
clock = pygame.time.Clock()
fps = 40

#GameLoop
i = 0
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                if main.gameRun == False:
                    main.start = False
                    main.gameRun = True
                    bird.bird_rect.centery = 200
                    bird.velocity = 0
                    main.score = 0
            if event.key == pygame.K_DOWN:
                bird.velocity = 0
                bird.velocity -= 10
        if event.type == pygame.MOUSEBUTTONDOWN:
            if main.gameRun == False:
                if pygame.mouse.get_pressed(3)[0] == 1:
                    main.start = False
                    main.gameRun = True
                    bird.bird_rect.centery = 200
                    bird.velocity = 0
                    main.score = 0
        if event.type == changePic:
            if bird.bird_rect.bottom < 480:
                i += 1
                if i > 3:
                    i = 0
    
    main.gameisrunning()
    pygame.display.update()
    clock.tick(fps)