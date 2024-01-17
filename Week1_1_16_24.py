import pygame

pygame.init()
screen = pygame.display.set_mode([800, 600])

apple_img = pygame.image.load("Apple.png")

runGame = True

while runGame:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runGame = False

    screen.blit(apple_img, (100, 100))
    pygame.display.update()
    
pygame.quit()
