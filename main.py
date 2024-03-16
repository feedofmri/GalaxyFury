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
VEL = 1

WIDTH, HEIGHT = 1066, 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Galaxy Fury")



def draw_screen(spe1, spe2):
    SCREEN.fill(WHITE)
    SCREEN.blit(SPACESHIP_1, (spe1.x, spe1.y))
    SCREEN.blit(SPACESHIP_3, (spe2.x, spe2.y))
    pygame.display.update()
    
    
def move_spe1(spe1, key):
    if key[pygame.K_w] and spe1.y - VEL > 0:
            spe1.y -= VEL
    if key[pygame.K_s] and spe1.y + VEL + spe1.height < HEIGHT:
            spe1.y += VEL
    if key[pygame.K_a] and spe1.x - VEL > 0:
            spe1.x -= VEL
    if key[pygame.K_d] and spe1.x + VEL + spe1.width < WIDTH:
        spe1.x += VEL
        
def move_spe2(spe2, key):
    if key[pygame.K_UP] and spe2.y - VEL > 0:
            spe2.y -= VEL
    if key[pygame.K_DOWN] and spe2.y + VEL + spe2.height < HEIGHT:
            spe2.y += VEL
    if key[pygame.K_LEFT] and spe2.x - VEL > 0:
            spe2.x -= VEL
    if key[pygame.K_RIGHT] and spe2.x + VEL + spe2.width < WIDTH:
            spe2.x += VEL


def main():
    
    spe1 = pygame.Rect(50, 250, 90, 91)
    spe2 = pygame.Rect(916, 250, 90, 100)
    clock = pygame.time.Clock()
    clock.tick(FPS)
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        key = pygame.key.get_pressed()
        
        move_spe1(spe1, key)
        move_spe2(spe2, key)
        draw_screen( spe1, spe2)
    pygame.quit()

if __name__ == "__main__":
    main()