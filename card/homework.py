import pygame
import sys
pygame.init()
WIDTH = 500
HEIGHT = 500
timer = 100

class Rect():
    def __init__(self,x,y,color,radius,width):
        self.screen = pygame.display.set_mode((WIDTH,HEIGHT))
        self.x=x
        self.y=y
        self.color=color
        self.radius=radius
        self.width=width
    def draw(self):
        pygame.draw.rect(self.screen,'black',(self.x,self.y,self.radius*5,self.radius))
        pygame.draw.rect(self.screen,self.color,(self.x+5,self.y+5,self.radius*5-10,self.radius-10),)
        
class Circle():
    def __init__(self,x,y,color,radius,width):
        self.screen = pygame.display.set_mode((WIDTH,HEIGHT))
        pygame.display.set_caption('LightBlub Simulation')
        self.x=x
        self.y=y
        self.color=color
        self.radius=radius
        self.width=width
    def draw(self):
        self.screen.fill('white')
        pygame.draw.circle(self.screen,self.color,(self.x,self.y),self.radius)
        pygame.draw.circle(self.screen,'black',(self.x,self.y),self.radius,self.width)
        
blub = Circle(WIDTH/2,HEIGHT/2-100,'grey',100,5)
switch = Rect(WIDTH/2-125,HEIGHT-HEIGHT/4,'White',50,10)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if timer != 0:
            timer = timer - 1
                    


    blub.draw()
    switch.draw()
    if event.type == pygame.MOUSEBUTTONDOWN:
        x,y = pygame.mouse.get_pos()
        if x > 125 and x < 375:
            if y < 425 and y > 375:
                if timer == 0:
                    timer = 10
                    if blub.color == 'grey':
                        blub.color = 'yellow'
                    elif blub.color == 'yellow':
                        blub.color = 'grey'
        
                    


    pygame.display.flip()
pygame.quit()
sys.exit()