
import sys, pygame
import random
import os
from pipe import Pipe
from bird import Player
import time

#explain what actor does

# Screen dimensions
WIDTH = 900
HEIGHT = 600


# Frame updates per second
FPS = 30 # use with clock 

# RGB colors of items on screen

BACKGROUND_COLOR = (0, 0, 0) # black
SCORE_COLOR = (255, 255, 255) # bright yellow

FileNotFoundError_RADIUS = 5
SPEED = 5
BIRD_COLOR = ( 0, 255, 255)
BIRD_RADIUS = 25

PIPE_COLOR = (0, 0, 255) # for now, later random colors 

ITEM_COLOR = (0, 255, 0)  




pygame.init() # initalize all pygame modules

#font for the score
font = pygame.font.SysFont("Arial", 22)


screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Flappy bird by Berket")

# create a clock object to mark time
clock = pygame.time.Clock()

def main(): # the game loop
    pipe_crossed = 0
    running = True
    


    #instiate screen objects -- 2 paddles, one ball
    bird = Player(WIDTH//2, HEIGHT//2, BIRD_RADIUS, SPEED, BIRD_COLOR)
    bird.direction = 0 
    pipe = Pipe(200, 3 ,5, 10, 100, 10, PIPE_COLOR)

    
    

    while running:
    
        screen.fill(BACKGROUND_COLOR)
        pygame.draw.rect(screen, (255, 255, 255), (WIDTH//2, 0, 10, HEIGHT))
        
        pipe.move()
        
        pipe.draw(screen)
        
        bird.draw(screen)
              
             
        

        bird.update(bird.direction)
        
        left_bottom_edge = bird.y + bird.radius
        print(left_bottom_edge)
        print(HEIGHT)
        if bird.y < 0:
            bird.y = 2
            bird.direction = 0

        if left_bottom_edge > HEIGHT-bird.radius:
            
            bird.direction = 0

        pygame.display.flip() # update the display
        clock.tick(FPS) # limit the frame rate to FPS
    
        # Event handling -- check for all events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("bye")
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_0:
                    print("zero key hit wooHOO")
                
                if event.key == pygame.K_w:
                    bird.direction = -1
                    
                    print("going up")
                    
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w or event.key == pygame.K_s:
                    bird.direction = 0.5
                    print("stopped moving")
                

if __name__ == "__main__":
    main()
    pygame.quit()