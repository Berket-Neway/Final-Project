import sys, pygame

class Pipe:
    def __init__(self, x, dx, y, width, height, speed, color):
        self.x = x
        self.dx = dx
        self.y = y
        self.width = width
        self.height = height
        self.speed = speed
        self.color = color
        

        self.rect = pygame.Rect(x, y, width, height)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
    
    
    def update(self):
        # self.rect.x -= self.scroll_speed
        # if self.rect.right < 0:
        #     print("your done")
        pass

    def move(self):
        self.x -= self.dx
        self.rect.x = self.x
        
