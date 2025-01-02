import pygame
import time
from random import randint
pygame.init()

WIDTH =600
HEIGHT =600
screen = pygame.display.set_mode((WIDTH,HEIGHT))
colour = [randint(0,255),randint(0,255),randint(0,255)]
pygame.display.set_caption('untitled for the current time while I am creating this thingamabob')

#load the images
image1 = pygame.image.load('images/page1.jpg')
image2 = pygame.image.load('images/page2.jpg')
image3 = pygame.image.load('images/page3.jpg')

#scaling the images
image1_size = pygame.transform.scale(image1,(WIDTH,HEIGHT))
image2_size = pygame.transform.scale(image2,(WIDTH,HEIGHT))
image3_size = pygame.transform.scale(image3,(WIDTH,HEIGHT))
list_of_images = [image1,image2,image3]
index = 0

#prepare text
font = pygame.font.SysFont('comic sans',50)
ohio_text = font.render('have a skibidi rizzday',True,colour)
text = ohio_text.get_rect(center = (WIDTH/2,HEIGHT/2))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    colour = [randint(0,255),randint(0,255),randint(0,255)]
    screen.fill('black')
    screen.blit(list_of_images[index],(0,0))
    time.sleep(2)
    if index >= 3:
        index = 0
    else:
        index = (index + 1)%len(list_of_images)
    screen.blit(ohio_text,text)

    pygame.display.update()


pygame.quit()