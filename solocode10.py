import pygame
import random
import sys
import pygwidgets


WINDOW_WIDTH = 600
WINDOW_HEIGHT = 800
FPS = 60

PLAYER_SPEED = 7
OBJECT_MIN_SPEED = 10
OBJECT_MAX_SPEED = 10

SPAWN_INTERVAL_MS = 800
DIFFICULTY_INTERVAL_MS = 7000  


class Player:
    def __init__(self, window):
        self.window = window
        self.width = 60
        self.height = 40
        self.x = WINDOW_WIDTH // 2 - self.width // 2
        self.y = WINDOW_HEIGHT - 100
        self.color1 = (50, 200, 255)
        self.color2 = (0, 150, 220)
        self.currentColor = self.color1

        self.animationInterval = 150
        self.lastAnimationTime = pygame.time.get_ticks()

       
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def handle_input(self, keys):
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.x -= PLAYER_SPEED
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.x += PLAYER_SPEED


        if self.x < 0:
            self.x = 0
        if self.x + self.width > WINDOW_WIDTH:
            self.x = WINDOW_WIDTH - self.width

        self.rect.topleft = (self.x, self.y)

    def update_animation(self):
        now = pygame.time.get_ticks()
        if now - self.lastAnimationTime >= self.animationInterval:
            self.lastAnimationTime = now
           
            if self.currentColor == self.color1:
                self.currentColor = self.color2
            else:
                self.currentColor = self.color1

    def draw(self):
        pygame.draw.rect(self.window, self.currentColor, self.rect)


class FallingObject:
    def __init__(self, window, speed):
        self.window = window
        self.radius = random.randint(15, 30)
        self.x = random.randint(self.radius, WINDOW_WIDTH - self.radius)
        self.y = -self.radius
        self.speed = speed
        self.color = (255, random.randint(80, 200), random.randint(80, 200))
        self.rect = pygame.Rect(self.x - self.radius,
                                self.y - self.radius,
                                self.radius * 2,
                                self.radius * 2)

    def update(self):
        self.y += self.speed
        self.rect.center = (self.x, self.y)

    def is_off_screen(self):
        return self.y - self.radius > WINDOW_HEIGHT

    def draw(self):
        pygame.draw.circle(self.window, self.color, (self.x, self.y), self.radius)



class DodgeGame:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Dodge the Falling Objects")
        self.clock = pygame.time.Clock()

        self.backgroundColor = (15, 15, 30)

        # pygwidgets UI elements
        self.scoreText = pygwidgets.DisplayText(self.window,
                                  (20, 20),
                                 "Score: 0",
                                  fontSize=28,
                                             textColor=(255, 255, 255))
        self.infoText = pygwidgets.DisplayText(self.window,
                                      (20, 60),
                                       "Use arrow keys or A/D to move",
                                       fontSize=22,
                                                   textColor=(200, 200, 200))
        self.gameOverText = pygwidgets.DisplayText(self.window,
                                         (WINDOW_WIDTH // 2 - 140, WINDOW_HEIGHT // 2 - 80),
                                           "",
                                           fontSize=40,
                                           textColor=(255, 80, 80))
        self.restartButton = pygwidgets.TextButton(self.window,
                                           (WINDOW_WIDTH // 2 - 80, WINDOW_HEIGHT // 2),
                                             "Restart",
                                           width=160,
                                           height=50)

        self.player = Player(self.window)
        self.objects = []

        
        self.lastSpawnTime = pygame.time.get_ticks()
        self.lastDifficultyTime = pygame.time.get_ticks()
        self.spawnInterval = SPAWN_INTERVAL_MS
        self.objectSpeedMin = OBJECT_MIN_SPEED
        self.objectSpeedMax = OBJECT_MAX_SPEED

      
        self.startTime = pygame.time.get_ticks()
        self.gameOver = False
        self.finalScore = 0

    def spawn_object(self):
        speed = random.randint(self.objectSpeedMin, self.objectSpeedMax)
        obj = FallingObject(self.window, speed)
        self.objects.append(obj)

    def increase_difficulty(self):
       
        if self.spawnInterval > 300:
            self.spawnInterval -= 80
        self.objectSpeedMin += 1
        self.objectSpeedMax += 1

    def reset_game(self):
        self.player = Player(self.window)
        self.objects = []
        self.lastSpawnTime = pygame.time.get_ticks()
        self.lastDifficultyTime = pygame.time.get_ticks()
        self.spawnInterval = SPAWN_INTERVAL_MS
        self.objectSpeedMin = OBJECT_MIN_SPEED
        self.objectSpeedMax = OBJECT_MAX_SPEED
        self.startTime = pygame.time.get_ticks()
        self.gameOver = False
        self.finalScore = 0
        self.gameOverText.setValue("")

    def update_score(self):
        if not self.gameOver:
            now = pygame.time.get_ticks()
            elapsed_ms = now - self.startTime
            seconds = elapsed_ms // 1000
            self.scoreText.setValue(f"Score: {seconds}")
            return seconds
        else:
            return self.finalScore

    def run(self):
        while True:
          
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if self.gameOver:
                    if self.restartButton.handleEvent(event):
                        self.reset_game()

            keys = pygame.key.get_pressed()
            if not self.gameOver:
                self.player.handle_input(keys)

            now = pygame.time.get_ticks()

            if not self.gameOver:
               
                if now - self.lastSpawnTime >= self.spawnInterval:
                    self.lastSpawnTime = now
                    self.spawn_object()

               
                if now - self.lastDifficultyTime >= DIFFICULTY_INTERVAL_MS:
                    self.lastDifficultyTime = now
                    self.increase_difficulty()

          
            if not self.gameOver:
                self.player.update_animation()

                for obj in self.objects:
                    obj.update()

               
                self.objects = [o for o in self.objects if not o.is_off_screen()]

               
                for obj in self.objects:
                    if self.player.rect.colliderect(obj.rect):
                        self.gameOver = True
                        self.finalScore = self.update_score()
                        self.gameOverText.setValue(f"Game Over! Score: {self.finalScore}")
                        break

            currentScore = self.update_score()

            self.window.fill(self.backgroundColor)

           
            for obj in self.objects:
                obj.draw()
            self.player.draw()

            
            self.scoreText.draw()
            self.infoText.draw()

            if self.gameOver:
                self.gameOverText.draw()
                self.restartButton.draw()

            pygame.display.update()
            self.clock.tick(FPS)


if __name__ == "__main__":
    game = DodgeGame()
    game.run()
