import pygame
import os

#team 1
SPACESHIP_1 = pygame.transform.scale(pygame.image.load(os.path.join("spaceship", "spaceship1.png")), (90, 91)) 
SPACESHIP_2 = pygame.transform.scale(pygame.image.load(os.path.join("spaceship", "spaceship2.png")), (90, 92)) 
#team 2
SPACESHIP_3 = pygame.transform.scale(pygame.image.load(os.path.join("spaceship", "spaceship3.png")), (90, 100)) 
SPACESHIP_4 = pygame.transform.scale(pygame.image.load(os.path.join("spaceship", "spaceship4.png")), (90, 79)) 

WHITE = (0, 0, 0)
FPS = 60

WIDTH, HEIGHT = 1066, 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Galaxy Fury")



def draw_screen():
    SCREEN.fill(WHITE)
    SCREEN.blit(SPACESHIP_1, (50, 250))
    SCREEN.blit(SPACESHIP_3, (916, 250))
    
    pygame.display.update()

def main():
    clock = pygame.time.Clock()
    clock.tick(FPS)
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        draw_screen()
    pygame.quit()

if __name__ == "__main__":
    main()