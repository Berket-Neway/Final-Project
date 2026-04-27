
import sys, pygame
import random
import os
from pipe import wall
from bird import Player
import time


# Screen dimensions
WIDTH = 900
HEIGHT = 600


# Frame updates per second
FPS = 30 # use with clock 

# RGB colors of items on screen

BACKGROUND_COLOR = (0, 0, 0) # black
SCORE_COLOR = (255, 255, 255) # bright yellow

FileNotFoundError_RADIUS = 5
DX_SPEED = 5
DY_SPEED = 5
SNAKE_COLOR = (255, 255, 255)


ITEM_COLOR = (0, 255, 0)  # for now, blue, later random colors 




pygame.init() # initalize all pygame modules

#font for the score
font = pygame.font.SysFont("Arial", 22)


screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Snake by Berket")

# create a clock object to mark time
clock = pygame.time.Clock()

def main(): # the game loop
    pipe_crossed = 0
    running = True
    


    #instiate screen objects -- 2 paddles, one ball
    ball = Ball(WIDTH//2, HEIGHT//2, BALL_RADIUS, DX_SPEED, DY_SPEED, BALL_COLOR)
    
    left_paddle = Paddle(20, 0, 10, 100, 10, L_PADDLE_COLOR)
    left_paddle.direction = 0 
    
    

    while running:
    
        screen.fill(BACKGROUND_COLOR)
        pygame.draw.rect(screen, (255, 255, 255), (WIDTH//2, 0, 10, HEIGHT))
        
        ball.move()
        ball.respond_to_edges(0, WIDTH, 0, HEIGHT)
        ball.respond_to_paddle(left_paddle)
       
        ball.draw(screen)
              
            
        l_text_surface = font.render(str(score_left), True, SCORE_COLOR)
        
        screen.blit(l_text_surface, (WIDTH//3.5, 20))
       
        
        
       
        left_paddle.update(left_paddle.direction)
        
        

        # RESPOND TO WALL AND PADDLE ---------
        
        left_paddle.display(screen)



        left_bottom_edge = left_paddle.y + left_paddle.height
        if left_paddle.y < 0:
            left_paddle.y = 2
            left_paddle.direction = 0

        if left_bottom_edge > HEIGHT:
            left_paddle.y = HEIGHT-left_paddle.height
            left_paddle.direction = 0

    
        



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
                    left_paddle.direction = -1
                    print("going up")
                    
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w or event.key == pygame.K_s:
                    left_paddle.direction = 1
                    print("stopped moving")
                

if __name__ == "__main__":
    main()
    pygame.quit()