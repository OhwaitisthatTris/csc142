import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH = 800
HEIGHT = 600
FPS = 60

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Set up the display
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Too Many Balls Game")
clock = pygame.time.Clock()

class Ball:
    def __init__(self, width, height):
        self.radius = 20
        self.x = random.randint(self.radius, width - self.radius)
        self.y = random.randint(self.radius, height - self.radius)
        self.dx = random.randint(-3, 3)
        self.dy = random.randint(-3, 3)
        self.color = (random.randint(100, 255), random.randint(100, 255), random.randint(100, 255))
        
    def update(self):
        self.x += self.dx
        self.y += self.dy
        
        if self.x <= self.radius or self.x >= WIDTH - self.radius:
            self.dx = -self.dx
        if self.y <= self.radius or self.y >= HEIGHT - self.radius:
            self.dy = -self.dy
    
    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (int(self.x), int(self.y)), self.radius)
    
    def was_clicked(self, pos):
        mouse_x, mouse_y = pos
        distance = ((mouse_x - self.x) ** 2 + (mouse_y - self.y) ** 2) ** 0.5
        return distance <= self.radius

def draw_text(surface, text, x, y, color, font_size=28):
    font = pygame.font.SysFont(None, font_size)
    text_surface = font.render(text, True, color)
    surface.blit(text_surface, (x, y))

# Game variables
ballList = []
score = 0
start_time = pygame.time.get_ticks()
lastSeconds = 0
game_over = False

# Start with one ball
ballList.append(Ball(WIDTH, HEIGHT))

# Main game loop
running = True
while running:
    dt = clock.tick(FPS)
    window.fill(BLACK)

    current_time = pygame.time.get_ticks()
    seconds_elapsed = (current_time - start_time) // 1000

    # Check for game over
    if seconds_elapsed >= 15:
        game_over = True
        ballList.clear()

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if not game_over and event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            for ball in ballList[:]:
                if ball.was_clicked(mouse_pos):
                    score += 1
                    ballList.remove(ball)

    # Add new ball every second
    if not game_over and seconds_elapsed != lastSeconds:
        ballList.append(Ball(WIDTH, HEIGHT))
        lastSeconds = seconds_elapsed

    # Update and draw balls
    if not game_over:
        for ball in ballList:
            ball.update()
            ball.draw(window)

    # Draw UI
    draw_text(window, f"Score: {score}", 10, 10, WHITE)
    draw_text(window, f"Time: {seconds_elapsed}", 10, 40, WHITE)

    if game_over:
        draw_text(window, "GAME OVER", WIDTH // 2 - 100, HEIGHT // 2 - 40, RED, 48)
        draw_text(window, f"Final Score: {score}", WIDTH // 2 - 120, HEIGHT // 2 + 10, WHITE, 36)

    pygame.display.update()

pygame.quit()
sys.exit()