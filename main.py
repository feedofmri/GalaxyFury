import pygame
import os

#team 1
SPACESHIP_1 = pygame.transform.scale(pygame.image.load(os.path.join("spaceship", "spaceship1.png")), (90, 91)) 
SPACESHIP_2 = pygame.transform.scale(pygame.image.load(os.path.join("spaceship", "spaceship2.png")), (90, 92)) 
#team 2
SPACESHIP_3 = pygame.transform.scale(pygame.image.load(os.path.join("spaceship", "spaceship3.png")), (90, 100)) 
SPACESHIP_4 = pygame.transform.scale(pygame.image.load(os.path.join("spaceship", "spaceship4.png")), (90, 79)) 

# bullet
BULLET_1 = pygame.transform.scale(pygame.image.load(os.path.join("bullet1.png")), (47, 15))
BULLET_2 = pygame.transform.scale(pygame.image.load(os.path.join("bullet2.png")), (46, 15))

BG = pygame.image.load(os.path.join("bg.png"))

WHITE = (255, 255, 255)
FPS = 60
VEL = 5
BULL_VEL = 10
MAX_BULLETS = 3
WIDTH, HEIGHT = 1066, 600
DEVIDER = pygame.Rect(WIDTH//2 - 3, 0, 6, HEIGHT)

SPE1_HIT = pygame.USEREVENT + 1
SPE2_HIT = pygame.USEREVENT + 2

SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Galaxy Fury")



def draw_screen(spe1, spe2):
    SCREEN.blit(BG, (0, 0))
    pygame.draw.rect(SCREEN, WHITE, DEVIDER)
    SCREEN.blit(SPACESHIP_1, (spe1.x, spe1.y))
    SCREEN.blit(SPACESHIP_3, (spe2.x, spe2.y))
    pygame.display.update()
    
    
    
def move_spe1(spe1, spe2, key):
        
    if key[pygame.K_w] and spe1.y - VEL > 0:
            spe1.y -= VEL
    if key[pygame.K_s] and spe1.y + VEL + spe1.height < HEIGHT:
            spe1.y += VEL
    if key[pygame.K_a] and spe1.x - VEL > 0:
            spe1.x -= VEL
    if key[pygame.K_d] and spe1.x + VEL + spe1.width < WIDTH/2 - 3:
        spe1.x += VEL
        
def move_spe2(spe1, spe2, key):
    if key[pygame.K_UP] and spe2.y - VEL > 0:
            spe2.y -= VEL
    if key[pygame.K_DOWN] and spe2.y + VEL + spe2.height < HEIGHT:
            spe2.y += VEL
    if key[pygame.K_LEFT] and spe2.x - VEL > WIDTH//2 + 3:
            spe2.x -= VEL
    if key[pygame.K_RIGHT] and spe2.x + VEL + spe2.width < WIDTH:
            spe2.x += VEL

def handle_bullets(spe1_bullets, spe2_bullets, spe1, spe2):
    for bullet in spe1_bullets:
        bullet.x += BULL_VEL
        if spe2.colliderect(bullet):
            pygame.event.post(pygame.event.Event(SPE2_HIT))
            spe1_bullets.remove(bullet)
        elif bullet.x > WIDTH:
            spe1_bullets.remove(bullet)
            
    for bullet in spe2_bullets:
        bullet.x -= BULL_VEL
        if spe1.colliderect(bullet):
            pygame.event.post(pygame.event.Event(SPE1_HIT))
            spe2_bullets.remove(bullet)
        elif bullet.x < 0:
            spe2_bullets.remove(bullet)
        
    for bullet in spe1_bullets:
        
        pygame.draw.rect(SCREEN, (255, 0, 0), bullet)
        
    for bullet in spe2_bullets:
        pygame.draw.rect(SCREEN, (0, 0, 255), bullet)
        
    pygame.display.update()


def main():
    
    spe1_bullets = []
    spe2_bullets = []
    
    spe1_life = 10
    spe2_life = 10
    
    spe1 = pygame.Rect(50, 250, 90, 91)
    spe2 = pygame.Rect(916, 250, 90, 100)
    clock = pygame.time.Clock()
    clock.tick(FPS)
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LSHIFT and len(spe1_bullets) < MAX_BULLETS:
                bullet = pygame.Rect(spe1.x + spe1.width, spe1.y + spe1.height//2 - 2, 10, 5)
                spe1_bullets.append(bullet)
                
                
            if event.key == pygame.K_RSHIFT and len(spe2_bullets) < MAX_BULLETS:
                bullet = pygame.Rect(spe2.x, spe2.y + spe2.height//2 - 2, 10, 5)
                spe2_bullets.append(bullet)
                  
        if spe1_life <= 0:
            print("Player 2 wins")
            running = False
        if spe2_life <= 0:
            print("Player 1 wins")
            running = False          
        
        if event.type == SPE1_HIT:
            spe1_life -= 1
        if event.type == SPE2_HIT:
            spe2_life -= 1
                                        
        key = pygame.key.get_pressed()
        
        print(spe1_bullets, spe2_bullets)
        
        handle_bullets(spe1_bullets, spe2_bullets, spe1, spe2)
        move_spe1(spe1, spe2, key)
        move_spe2(spe1, spe2, key)
        draw_screen( spe1, spe2)
        
    pygame.quit()

if __name__ == "__main__":
    main()