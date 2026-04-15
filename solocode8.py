import pygame
import random
import time


class Raindrop:
    __slots__ = ("x", "y", "radius")

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radius = 1

    def update(self):
        self.radius += 1

    def draw(self, window):
        pygame.draw.circle(window, (0, 100, 255), (self.x, self.y), self.radius, 2)



class RaindropsManager:
    RAIN_RATE = 0.2     
    MAX_RADIUS = 40      

    def __init__(self):
        pygame.init()
        self.width = 600
        self.height = 400
        self.window = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Raindrops Simulation")

        self.raindrops = []
        self.last_drop_time = time.time()
        self.running = True

    def add_raindrop(self):
        x = random.randint(0, self.width)
        y = random.randint(0, self.height)
        self.raindrops.append(Raindrop(x, y))

    def update_raindrops(self):
        for drop in self.raindrops:
            drop.update()

        
        self.raindrops = [d for d in self.raindrops if d.radius <= self.MAX_RADIUS]

    def draw_raindrops(self):
        for drop in self.raindrops:
            drop.draw(self.window)

    def run(self):
        clock = pygame.time.Clock()

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

           
            now = time.time()
            if now - self.last_drop_time >= self.RAIN_RATE:
                self.add_raindrop()
                self.last_drop_time = now

            self.update_raindrops()

            self.window.fill((20, 20, 20))
            self.draw_raindrops()
            pygame.display.flip()

            clock.tick(60)

        pygame.quit()


# -----------------------------------------
# Driver code
# -----------------------------------------
if __name__ == "__main__":
    manager = RaindropsManager()
    manager.run()
