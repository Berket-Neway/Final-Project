
import sys, pygame
import random
import os
from pipe import Pipe
from bird import Player
import time
import random


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
BIRD_COLOR = ( 0, 0, 0)
BIRD_RADIUS = 25

PIPE_COLOR = (0, 0, 66) # for now, later random colors 






pygame.init() # initalize all pygame modules

#font for the score
font = pygame.font.SysFont("Arial", 22)


screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Flappy bird by Berket")


help_image = pygame.image.load("assets/help.png").convert_alpha()
help_image = pygame.transform.scale(help_image, (150, 150))
help_image = pygame.transform.flip(help_image, True, False)
help_correct_image = pygame.image.load("assets/correct.png").convert_alpha()
help_correct_image = pygame.transform.scale(help_correct_image, (150, 150))
help_correct_image = pygame.transform.flip(help_correct_image, True, False)

help_incorrect_image = pygame.image.load("assets/wrong.png").convert_alpha()
help_incorrect_image = pygame.transform.scale(help_incorrect_image, (150, 200))
help_incorrect_image = pygame.transform.flip(help_incorrect_image, True, False)





# create a clock object to mark time
clock = pygame.time.Clock()

def main(): # the game loop
    pipe_crossed = 0
    running = True
    bird_health = 3


    #instiate screen objects -- 2 paddles, one ball
    bird = Player(WIDTH//2, HEIGHT//2, BIRD_RADIUS, SPEED, BIRD_COLOR)
    bird.direction = 0 
    pipe_gap_y = random.randint(100, HEIGHT - 100 - GAP)

    pipe = Pipe(WIDTH, 3, 2, 75, pipe_gap_y, 10, PIPE_COLOR, True)
    two_pipe = Pipe(WIDTH, 3, pipe_gap_y + GAP, 75, HEIGHT - (pipe_gap_y + GAP), 10, PIPE_COLOR, False)
    
    game_over = False
    begin_game = True
    help_screen = False
    while running:
        if begin_game and not help_screen:
            screen.fill((255, 0, 0))  # WHITE SCREEN

            text = font.render("Berket's Flappy Bird Clone", True, (0, 0, 0))
            begin_text = font.render("Click the SPACE KEY to begin", True, (0, 0, 0))
            help = f"Click the H key for Help"
            help_text= font.render(str(help), True, (0, 0, 0))

            screen.blit(text, (WIDTH//2 - 60, HEIGHT//2 - 30))
            screen.blit(begin_text, (WIDTH//2 - 85, HEIGHT//2 ))
            screen.blit(help_text,(WIDTH//2 - 110, HEIGHT//2 + 120))
            
            pygame.display.flip()
        
        elif help_screen:
            screen.fill((255, 255, 255))
            text = font.render("Explaination:", True, (0, 0, 0))
            begin_text = font.render("Click the SPACE KEY to EXIT", True, (0, 0, 0))
            help_1 = font.render("In this game, you are controlling a bird that must cross pipes,", True, (0, 0, 0))
            help_2 = font.render("use the W and S key to lead the bird through the pipes", True, (0, 0, 0))
            help_3 = font.render("W makes bird go up", True, (0, 0, 0))
            help_4 = font.render("S makes bird go down", True, (0, 0, 0))

            

            screen.blit(text, (35, 25))
            screen.blit(begin_text, (35, HEIGHT - 25))
            screen.blit(help_1,(35, 50 ))
            screen.blit(help_2,(35, 75 ))
            screen.blit(help_3,(35, 205))
            screen.blit(help_4,(35 ,275 ))
            screen.blit(help_image, (WIDTH-180, 50))
            screen.blit(help_correct_image, (WIDTH-180, 205))
            screen.blit(help_incorrect_image, (WIDTH-180, 360))
            pygame.display.flip()

     
        
        
    
        
        if game_over == False and begin_game == False:
            screen.fill(BACKGROUND_COLOR)
            
            
            bird.draw(screen)
            pipe.draw(screen)
            pipe.move()
            two_pipe.draw(screen)
            two_pipe.move()
            score_text = f"{pipe_crossed} |"
            score_surface = font.render(str(score_text), True, "white")
            screen.blit(score_surface, (WIDTH - 60, HEIGHT//2))
        

        bird.update(bird.direction)
        
        left_bottom_edge = bird.y + bird.radius
        
        if bird.y < 0:
            bird.y = 2
            bird.direction = 0

        if left_bottom_edge > HEIGHT-bird.radius:
            
            bird.direction = 0

      
        
        if bird.rect.colliderect(pipe):
            print("death")
            bird_health -= 1
        
     
        if bird.rect.colliderect(two_pipe) == True:
            print("death")
            bird_health -= 1
        print(pipe.x)
        
        if bird.rect.colliderect(pipe) == False and bird.rect.colliderect(two_pipe) == False and (pipe.x >= 450.0 and pipe.x <= 452.0) :
            print("pass")
            pipe_crossed += 1
            
            

        if pipe.x <= 0 and two_pipe.x <= 0:
            
            
            pipe.x = WIDTH
            pipe.rect.x = WIDTH
            two_pipe.x = WIDTH
            two_pipe.rect.x = WIDTH
            pipe_gap_y = random.randint(100, HEIGHT - 100 - GAP)
            pipe.rect.y = 0
            pipe.rect.height = pipe_gap_y
            pipe.image = pygame.transform.scale(pipe.image, (pipe.width, pipe.rect.height))
            two_pipe.image = pygame.transform.scale(pipe.image, (pipe.width, pipe.rect.height+pipe_gap_y + GAP))
            
            two_pipe.rect.y = pipe_gap_y + GAP
            two_pipe.rect.height = HEIGHT - (pipe_gap_y + GAP)


            pipe.dx += 0.1 * pipe_crossed
            two_pipe.dx += 0.1 *pipe_crossed
            
            


        pygame.display.flip() # update the display
        clock.tick(FPS) # limit the frame rate to FPS
    
        if bird.rect.colliderect(pipe.rect) or bird.rect.colliderect(two_pipe.rect):
            game_over = True
            pass

        # Event handling -- check for all events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("bye")
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_h and begin_game == True:
                    print("zero key hit wooHOO")
                    help_screen = True
                    
                                
                if event.key == pygame.K_r and game_over == True:
                    print("game is restarted???")
                    game_over = False
                    pipe.x = WIDTH + 15
                    two_pipe.x = WIDTH + 15
                    pipe_crossed = 0
                if event.key == pygame.K_w:
                    bird.direction = -1
                    print("going up")
                if event.key == pygame.K_s:
                    bird.direction = 1
                    print("going down")
                if event.key == pygame.K_SPACE and begin_game == True and help_screen == False:
                    begin_game = False
                    
                if event.key == pygame.K_SPACE and help_screen == True:
                    help_screen = False
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w or event.key == pygame.K_s:
                    bird.direction = 0.5
                    print("stopped moving")

        if game_over == True:
            screen.fill((255, 255, 255))  # WHITE SCREEN

            text = font.render("Game Over", True, (0, 0, 0))
            retry_text = font.render("Click the R KEY to restart", True, (0, 0, 0))
            death_score_text = f"Crossed {pipe_crossed} Pipes"
            death_score_surface = font.render(str(death_score_text), True, (0, 0, 0))

            screen.blit(text, (WIDTH//2 - 60, HEIGHT//2 - 30))
            screen.blit(death_score_surface, (WIDTH//2 - 85, HEIGHT//2 ))
            screen.blit(retry_text,(WIDTH//2 - 110, HEIGHT//2 + 120))
            
            pygame.display.flip()
            running = True
            

    
    
    






if __name__ == "__main__":
    main()
    
    # pygame.quit()