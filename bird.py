import sys, pygame
from pygame import mixer

HIT_COLOR = "black"

class Player:


    def __init__(self, x, y, radius, speed , color):
        self.x = x
        self.y = y
        self.radius = radius
        self.speed = speed
        self.color = color
        self.image = pygame.image.load("assets/bird.png").convert_alpha()
        

        width = 10
        height = 2*radius
        self.image = pygame.transform.scale(self.image, (self.radius *4 , self.radius*4))

        self.rect = pygame.Rect(self.x,self.y, width, height)

    def draw(self, canvas):
        pygame.draw.circle(canvas, self.color , (self.x, self.y+25), self.radius)
        
        canvas.blit(self.image, (self.x-45, self.y-28))
        
    
        
    
    def update(self, direction):
        self.y += self.speed * direction
        self.rect.y = self.y