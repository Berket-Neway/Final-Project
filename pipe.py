import sys, pygame

class Pipe:
    def __init__(self, x, dx, y, width, height, speed, color, flip):
        self.x = x
        self.dx = dx
        self.y = y
        self.width = width
        self.height = height
        self.speed = speed
        self.color = color
        self.image = pygame.image.load("assets/pipe.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.width, self.height)
        )
        

        self.rect = pygame.Rect(x, y, width, height)
        if flip == True:
            self.image = pygame.transform.flip(self.image, False, True)
            
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        screen.blit(self.image, (self.x, self.y))
    
    
    def update(self):
        # self.rect.x -= self.scroll_speed
        # if self.rect.right < 0:
        #     print("your done")
        pass

    def move(self):
        self.x -= self.dx
        self.rect.x = self.x
        
