import pygame
from settings import *
import random


def draw_background():
    screen.fill(BACKGROUND_COLOR)

def draw_grid():
    for i in range(30+SQUARE_SIZE//3, SQUARE_SIZE+20+1, SQUARE_SIZE//3):
        pygame.draw.line(screen, WHITE, (i,30), (i,SQUARE_SIZE+30), 3)
    for i in range(30+SQUARE_SIZE//3, SQUARE_SIZE+20+1, SQUARE_SIZE//3):
        pygame.draw.line(screen, WHITE, (30,i), (SQUARE_SIZE+30,i), 3)

    for i in range(0,3):
        for j in range(1,4):
            for k in range(30+SQUARE_SIZE//9*j, SQUARE_SIZE//3*j, SQUARE_SIZE//9):
                pygame.draw.line(screen, WHITE, (k,40+(SQUARE_SIZE//3)*i), (k,(SQUARE_SIZE//3)*(i+1)+20), 1)
            for k in range(30+SQUARE_SIZE//9*j, SQUARE_SIZE//3*j, SQUARE_SIZE//9):
                pygame.draw.line(screen, WHITE, (40+(SQUARE_SIZE//3)*i,k), ((SQUARE_SIZE//3)*(i+1)+20, k), 1)
       
    
def gen_matrix():
    # [ 
    #   [ [3*3] [3*3] [3*3] ] 
    #   [ [3*3] [3*3] [3*3] ] 
    #   [ [3*3] [3*3] [3*3] ] 
    # ]

    grid=



if __name__ == '__main__':
    pygame.init()
    clock=pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT), flags, vsync=1)
    pygame.display.set_caption('Snake♥')
    font = pygame.font.SysFont('arial', 20)


    selected=-1
    select_game=-1
    square_width=560
    direction=-1
    game_started=False
    game_ended=False
    points_count=0
    

    draw_background()
    draw_grid()


    run  = True
    selected_cell=(-1,-1)
    while run:
            
        for event in pygame.event.get():
            if (event.type == pygame.QUIT or (event.type==pygame.KEYDOWN and event.key==pygame.K_ESCAPE)):
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                x,y=pygame.mouse.get_pos()
               
            if (event.type == pygame.KEYDOWN):
                # up->0, right->1, down->2 left->3
               pass
        
        pygame.display.flip()
        clock.tick(30)
        

    pygame.quit()