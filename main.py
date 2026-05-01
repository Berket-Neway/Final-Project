
import sys, pygame
import random
import os
from pipe import Pipe
from bird import Player
import time
import random
#explain what actor does

# Screen dimensions
WIDTH = 900
HEIGHT = 600
GAP = 100

# Frame updates per second
FPS = 30 # use with clock 

# RGB colors of items on screen

BACKGROUND_COLOR = (0, 0, 0) # black
SCORE_COLOR = (255, 255, 255) # bright yellow


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
    pipe_gap_y = random.randint(100, HEIGHT - 100 - GAP)

    pipe = Pipe(WIDTH, 3 , 2, 10, pipe_gap_y, 10, PIPE_COLOR)
    two_pipe = Pipe(WIDTH, 3 ,pipe_gap_y+ GAP, 10, HEIGHT - (pipe_gap_y + GAP), 10, "red")
    
    

    while running:

        
        
        screen.fill(BACKGROUND_COLOR)
        pygame.draw.rect(screen, (255, 255, 255), (WIDTH//2, 0, 10, HEIGHT))
        
        
        
        
   
        bird.draw(screen)
           
        pipe.draw(screen)
        pipe.move()
        two_pipe.draw(screen)
        two_pipe.move()
        

        bird.update(bird.direction)
        
        left_bottom_edge = bird.y + bird.radius
        
        if bird.y < 0:
            bird.y = 2
            bird.direction = 0

        if left_bottom_edge > HEIGHT-bird.radius:
            
            bird.direction = 0

      
        
        if bird.rect.colliderect(pipe):
            print("death")
        
     
        if bird.rect.colliderect(two_pipe) == True:
            print("death")

        if bird.rect.colliderect(pipe) == False and bird.rect.colliderect(two_pipe) == False and pipe.x == bird.x:
            print("pass")

        if pipe.x == 0 and two_pipe.x == 0:
            pipe.x = WIDTH
            two_pipe.x = WIDTH
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