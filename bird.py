import sys, pygame
from pygame import mixer

HIT_COLOR = "red"

class Player:


    def __init__(self, x, y, radius, speed , color):
        self.x = x
        self.y = y
        self.radius = radius
        self.speed = speed
        self.color = color
        
        width = 10
        height = 2*radius
        

        self.rect = pygame.Rect(self.x,self.y, width, height)

    def draw(self, canvas):
        pygame.draw.circle(canvas, self.color , (self.x, self.y+25), self.radius)
    
        pygame.draw.rect(canvas, HIT_COLOR , self.rect)
    
    def update(self, direction):
        self.y += self.speed * direction
        self.rect.y = self.y