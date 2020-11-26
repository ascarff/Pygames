## TicTacToe game based upon the TechVidvan tutorial from here: https://techvidvan.com/tutorials/python-game-project-tic-tac-toe/comment-page-1/

import pygame as pg,sys
from pygame.locals import * 
import time

#Initialise global variables
YB = 'yellow'
winner = None
draw = False
width = 700
height = 600
white = (255, 255, 255)
lineColour = (10, 10, 10)

#TicTacToe 7x6 board
C4 = [[None]*6, [None]*6, [None]*6, [None]*6, [None]*6, [None]*6, [None]*6]

#Initialise pygame window
pg.init()
fps = 30
CLOCK = pg.time.Clock()
screen = pg.display.set_mode((width, height+100), 0, 32)
pg.display.set_caption("Align More Than Three")

#Load images
opening = pg.image.load('Connect4_Opening.png')
yellow_img = pg.image.load('Yellow.png')
blue_img = pg.image.load('Blue.png')

#resize images
yellow_img = pg.transform.scale(yellow_img, (80,80))
blue_img = pg.transform.scale(blue_img, (80,80))
opening = pg.transform.scale(opening, (width, height+100))

def game_opening():
    screen.blit(opening, (0,0))
    pg.display.update()
    time.sleep(3)
    screen.fill(white)

    #Draw vertical lines
    pg.draw.line(screen, lineColour, (width/7,0), (width/7,height), 7)
    pg.draw.line(screen, lineColour, (width/7*2,0), (width/7*2,height), 7)
    pg.draw.line(screen, lineColour, (width/7*3,0), (width/7*3,height), 7)
    pg.draw.line(screen, lineColour, (width/7*4,0), (width/7*4,height), 7)
    pg.draw.line(screen, lineColour, (width/7*5,0), (width/7*5,height), 7)
    pg.draw.line(screen, lineColour, (width/7*6,0), (width/7*6,height), 7)
    #Draw horizontal lines
    pg.draw.line(screen, lineColour, (0,height/6), (width,height/6), 7)
    pg.draw.line(screen, lineColour, (0,height/6*2), (width,height/6*2), 7)
    pg.draw.line(screen, lineColour, (0,height/6*3), (width,height/6*3), 7)
    pg.draw.line(screen, lineColour, (0,height/6*4), (width,height/6*4), 7)
    pg.draw.line(screen, lineColour, (0,height/6*5), (width,height/6*5), 7)
    draw_status()

def draw_status():
    global draw

    if winner is None:
        message = YB.upper() + "'s Turn"
    else:
        message = winner.upper() + " won!"
    
    if draw:
        message = 'Game Drawn!'

        
    font = pg.font.Font(None, 30)
    text = font.render(message, 1, (255, 255, 255))

    #Copy the rendered message onto the board
    screen.fill((0, 0, 0), (0, height, width, 100))
    text_rect = text.get_rect(center=(width/2, height+50))
    screen.blit(text, text_rect)
    pg.display.update()

def check_win():
    global C4, winner, draw

    #Check for winning rows
    for row in range(0,6):
        for col in range(0,4):
            if((C4[col][row] == C4[col+1][row] == C4[col+2][row] == C4[col+3][row]) and (C4[col][row] is not None)):
                #winnerwinner
                winner = C4[col][row]
                #Draw winning line
                pg.draw.line(screen, (250,0,0), ((width/7*(col)), (row+1)*height/6 - height/12), \
                                 ((width/7*(col+4)), (row+1)*height/6-height/12), 4)
                break

    # check for winning columns
    for col in range (0, 7):
        for row in range(0,3):
            if (C4[col][row+0] == C4[col][row+1] == C4[col][row+2] == C4[col][row+3]) and (C4[col][row] is not None):
                # this column won
                winner = C4[col][row]
                #draw winning line
                pg.draw.line (screen, (250,0,0),((col + 1)* width/7 - width/14, height/6*row),\
                                  ((col + 1)* width/7 - width/14, height/6*(row+4)), 4)
                break


    for col in range(0,7):
        for row in range(0,6):
            if(col<4 and row <3):
                if (C4[col][row] == C4[col+1][row+1] == C4[col+2][row+2] == C4[col+3][row+3]) and (C4[col][row] is not None):
                    winner = C4[col][row]
                    pg.draw.line (screen, (250,0,0),((col)* width/7, (row) * height/6),\
                                      ((col + 4)* width/7, height/6*(row + 4)), 4)
                    break
            elif(col>2 and row<3):
                if (C4[col][row] == C4[col-1][row+1] == C4[col-2][row+2] == C4[col-3][row+3]) and (C4[col][row] is not None):
                    winner = C4[col][row]
                    pg.draw.line (screen, (250,0,0),((col+1 )* width/7, (row )* height/6),\
                                      ((col - 3)* width/7, height/6*(row + 4)), 4)
                    break
            elif(col<4 and row>2):
                if (C4[col][row] == C4[col+1][row-1] == C4[col+2][row-2] == C4[col+3][row-3]) and (C4[col][row] is not None):
                    winner = C4[col][row]
                    pg.draw.line (screen, (250,0,0),((col)* width/7, (row + 1)* height/6),\
                                      ((col + 4)* width/7, height/6*(row - 3)), 4)
                    break
            elif(col>2 and row>2):
                if (C4[col][row] == C4[col-1][row-1] == C4[col-2][row-2] == C4[col-3][row-3]) and (C4[col][row] is not None):
                    winner = C4[col][row]
                    pg.draw.line (screen, (250,0,0),((col + 1)* width/7, (row + 1) * height/6),\
                                      ((col - 3)* width/7, height/6*(row - 3)), 4)
                    break
            else:
                continue

    if(all([all(row) for row in C4]) and winner is None):
            draw = True

        
    draw_status()


"""
    # check for diagonal winners
        if (C4[0][0] == C4[1][1] == C4[2][2]) and (C4[0][0] is not None):
            # game won diagonally left to right
            winner = C4[0][0]
            pg.draw.line (screen, (250,70,70), (50, 50), (350, 350), 4)

        if (C4[0][2] == C4[1][1] == C4[2][0]) and (C4[0][2] is not None):
            # game won diagonally right to left
            winner = C4[0][2]
            pg.draw.line (screen, (250,70,70), (350, 50), (50, 350), 4)

        if(all([all(row) for row in C4]) and winner is None):
            draw = True
"""

def drawYB(col,row):
    global C4, YB
    if row ==1:
        posy = 10
    if row==2:
        posy = height/6+10
    if row==3:
        posy = height/6*2+10
    if row==4:
        posy = height/6*3+10
    if row==5:
        posy = height/6*4+10
    if row==6:
        posy = height/6*5+10

    if col==1:
        posx = 10
    if col==2:
        posx = width/7+10
    if col==3:
        posx = width/7*2+10
    if col==4:
        posx = width/7*3+10
    if col==5:
        posx = width/7*4+10
    if col==6:
        posx = width/7*5+10
    if col==7:
        posx = width/7*6+10

    C4[col-1][row-1] = YB
    if(YB == 'yellow'):
        screen.blit(yellow_img, (posx, posy))
        YB = 'blue'
    else:
        screen.blit(blue_img, (posx,posy))
        YB = 'yellow'
    pg.display.update()


def userClick():
    #Get click coords
    x, y = pg.mouse.get_pos()

    #Get click column
    if (x<width/7):
        col=1
    elif(x<width/7*2):
        col=2
    elif(x<width/7*3):
        col=3
    elif(x<width/7*4):
        col=4
    elif(x<width/7*5):
        col=5
    elif(x<width/7*6):
        col=6
    elif(x<width):
        col=7
    else:
        col=None

    for i in reversed(range(0,6)):
        if (C4[col-1][i] is None):
            row = i+1
            break

    if (row and col and C4[col-1][row-1] is None):
        global YB
        #Draw Y or B
        drawYB(col,row)
        check_win()

"""
    #get row of mouse click (1-3)
    if(y<height/6):
        row = 1
    elif (y<height/6*2):
        row = 2
    elif (y<height/6*3):
        row = 3
    elif (y<height/6*4):
        row = 4
    elif (y<height/6*5):
        row = 5
    elif(y<height):
        row = 6
    else:
        row = None

    if (row and col and C4[col-1][row-1] is None):
        global YB

        #Draw X or O
        drawYB(row,col)
        check_win()
"""
def reset_game():
    global C4, winner, YB, draw
    time.sleep(3)
    YB = 'yellow'
    draw = False
    game_opening()
    winner = None
    draw_status()
    C4 = [[None]*6, [None]*6, [None]*6, [None]*6, [None]*6, [None]*6, [None]*6]


game_opening()

#Run the game. Forever!
while(True):
    for event in pg.event.get():
        if event.type == QUIT:
            pg.quit()
            sys.exit()
        elif event.type == MOUSEBUTTONDOWN:
            userClick()
            if(winner or draw):
                reset_game()

    pg.display.update()
    CLOCK.tick(fps)
