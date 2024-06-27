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
        
def gen_grid():
    # [ 
    #   [ [3*3] [3*3] [3*3] ] 
    #   [ [3*3] [3*3] [3*3] ] 
    #   [ [3*3] [3*3] [3*3] ] 
    # ]

    grid=[]
    for i in range(9):
        temp=[]
        for j in range(9):
            temp.append(0)
        grid.append(temp)
    return grid

def show_grid():
    for i in range (len(grid)):
        for j in range (len(grid[i])):
            pygame.draw.rect(screen, RED, ())

def draw_symbol(row, col, player):
    if(grid[row][col]==0):
        y=row*(SQUARE_SIZE/9)+30
        x=col*(SQUARE_SIZE/9)+30
        if player:
            print(x,y)
            pygame.draw.circle(screen, RED, (x+30,y+30), 20, 6)
            grid[row][col]=1
        else:
            # pygame.draw.rect(screen, BLUE, (x,y,10,10))
            offset1=12
            offset2=18
            pygame.draw.polygon(screen, BLUE, [(x+offset1, y+offset2), (x+offset2, y+offset1), (x+(SQUARE_SIZE/9)-offset1, y+(SQUARE_SIZE/9)-offset2), (x+(SQUARE_SIZE/9)-offset2, y+(SQUARE_SIZE/9)-offset1) ])
            pygame.draw.polygon(screen, BLUE, [(x+(SQUARE_SIZE/9)-offset2, y+offset1), (x+(SQUARE_SIZE/9)-offset1, y+offset2), (x+offset2, y+(SQUARE_SIZE/9)-offset1), (x+offset1, y+(SQUARE_SIZE/9)-offset2) ])
            grid[row][col]=2
        check_win(row, col)

def other_player():
    valid_choice=[]
    for row in range (len(grid)):
        for col in range(len(grid[row])):
            if(grid[row][col]==0):
                valid_choice.append((row,col))
    row,col=random.choice(valid_choice)
    draw_symbol(row,col,False)




    # row=random.randint(0,8)
    # col=random.randint(0,8)
    # while(grid[row][col]!=0):
    #     row=random.randint(0,8)
    #     col=random.randint(0,8)   
       
def check_win(row, col):
    for i in 




if __name__ == '__main__':
    pygame.init()
    clock=pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT), flags, vsync=1)
    pygame.display.set_caption('Snake♥')
    font = pygame.font.SysFont('arial', 20)


    selected=-1
    select_game=-1
    direction=-1
    game_started=False
    game_ended=False
    points_count=0
    

    draw_background()
    draw_grid()
    grid=gen_grid()


    run  = True
    selected_cell=(-1,-1)
    while run:
            
        for event in pygame.event.get():
            if (event.type == pygame.QUIT or (event.type==pygame.KEYDOWN and event.key==pygame.K_ESCAPE)):
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                x,y=pygame.mouse.get_pos()
                if (x>=30 and x<=SQUARE_SIZE+30 and y>=30 and y<=SQUARE_SIZE+30):
                    col=(x-30)//(SQUARE_SIZE//9)
                    row=(y-30)//(SQUARE_SIZE//9)
                    draw_symbol(row, col, True)  
                    other_player()                  
            if (event.type == pygame.KEYDOWN):
                # up->0, right->1, down->2 left->3
               pass
        
        pygame.display.flip()
        clock.tick(30)
        

    pygame.quit()