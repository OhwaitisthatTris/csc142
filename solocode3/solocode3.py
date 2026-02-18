# pygame demo 4(c), one image, bounce around the window - with sound

# 1 - Import packages
import pygame
from pygame.locals import *
import sys
import random

def draw_text(surface, text, x, y, color, font_size=24):
    text_font = pygame.font.SysFont(None, font_size)
    text_surface = text_font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.topleft = (x, y)
    surface.blit(text_surface, text_rect)

# 2 - Define constants
BLACK = (0, 0, 0)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30
N_PIXELS_PER_FRAME = 3

# 3 - Initialize the world
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()
 
# 4 - Load assets: image(s), sound(s),  etc.
ballImage = pygame.image.load('solocode3/images/ball.png')
bounceSound = pygame.mixer.Sound('solocode3/sounds/boing.wav')
pygame.mixer.music.load('solocode3/sounds/background.mp3')
pygame.mixer.music.play(-1, 0.0)


# 5 - Initialize variables
ballRect = ballImage.get_rect()
MAX_WIDTH = WINDOW_WIDTH - ballRect.width
MAX_HEIGHT = WINDOW_HEIGHT - ballRect.height
ballRect.left = random.randrange(MAX_WIDTH)
ballRect.top = random.randrange(MAX_HEIGHT)
xSpeed = N_PIXELS_PER_FRAME
ySpeed = N_PIXELS_PER_FRAME
 
start_time = pygame.time.get_ticks() 
score = 0
Game_over = False

while True:


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
       
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos

            if ballRect.collidepoint(mouse_x, mouse_y):
             print("Ball clicked!")
            score += 1
   
    if (ballRect.left < 0) or (ballRect.right >= WINDOW_WIDTH):
        xSpeed = -xSpeed  
        bounceSound.play()

    if (ballRect.top < 0) or (ballRect.bottom >= WINDOW_HEIGHT):
        ySpeed = -ySpeed  
        bounceSound.play()

   
    ballRect.left = ballRect.left + xSpeed
    ballRect.top = ballRect.top + ySpeed

 
    window.fill(BLACK)
    

    window.blit(ballImage, ballRect)

 
    pygame.display.update()


    clock.tick(FRAMES_PER_SECOND)  

