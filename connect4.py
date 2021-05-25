##
## Darren Cronover
## Connect 4
##
##################

#Import Libraries
import pygame, sys, math, numpy
from pygame.locals import *

#Some color Variables
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
TEAL = (0, 125, 125)
COLORS = [BLACK, WHITE, GREEN, RED, TEAL]

def create_board(NUM_ROWS, NUM_COLUMNS):
#Makes a 6x7 INDEXED list of zeroes
    board=numpy.zeros((NUM_ROWS,NUM_COLUMNS))
    return board

def place_piece(board, row, col, piece):
#Takes the piece (whichever player has a turn) and places it in the correct part of the boards list
    board[row][col] = piece

def valid_move(board, col, NUM_ROWS):
#Compares the move to the top row of the board to look for an open space in that COLUMN
    return board[NUM_ROWS-1][col] == 0

def valid_row(board, col, NUM_ROWS):
#Determines the ROWS that are open and valid to be played in
    for r in range(NUM_ROWS):
        if board[r][col] == 0:
            return r

def is_winning_move(board, piece, NUM_ROWS, NUM_COLUMNS):
#Check for 4 in a row, only in the necessary rows/columns
    #Check horizontal locations for win
    for c in range(NUM_COLUMNS-3):# -3 because the last 3 columns can not have a winning horizontal move START in them
        for r in range(NUM_ROWS):
            #Checks for 4 in a row
            if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3]==piece:
                return True
            
    #Check vertical locations for win
    for c in range(NUM_COLUMNS):# 3 because the last 3 rows can not have a winning vertical move START in them
        for r in range(NUM_ROWS-3):
            if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c]==piece:
                return True

    #Check for diagonals with POSITIVE slope
    for c in range(NUM_COLUMNS-3):
        for r in range(NUM_ROWS-3): #Checks up til 3rd from last row, then rows and columns increase
            if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3]==piece:
                return True
            
    #Check for diagonals with NEGATIVE slope
    for c in range(NUM_COLUMNS-3):
        for r in range(3, NUM_ROWS): #Checks between row 4 and the final row - then rows decrease and col increase
            if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3]==piece:
                return True
            
def draw_board(screen, board, NUM_ROWS, NUM_COLUMNS, BLOCK_SIZE, RADIUS, SCR_HEI):
#Displays the board to the pygame window
    #The board size can be changed by altering the constants in main()
    for c in range(NUM_COLUMNS):
        for r in range(NUM_ROWS): #Creates teal squares with black circles inside them
            pygame.draw.rect(screen, COLORS[4], (c*BLOCK_SIZE, r*BLOCK_SIZE+BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
            pygame.draw.circle(screen, COLORS[0], (int(c*BLOCK_SIZE+BLOCK_SIZE/2), int(r*BLOCK_SIZE+BLOCK_SIZE+BLOCK_SIZE/2)), RADIUS)
    for c in range(NUM_COLUMNS):
            for r in range(NUM_ROWS): #Creates a red or green circle in a row/column based on user input
                if board[r][c] == 1: 
                    pygame.draw.circle(screen, COLORS[3], (int(c*BLOCK_SIZE+BLOCK_SIZE/2), SCR_HEI -   int(r*BLOCK_SIZE+BLOCK_SIZE/2)), RADIUS)
                elif board[r][c] == 2:
                    pygame.draw.circle(screen, COLORS[2], (int(c*BLOCK_SIZE+BLOCK_SIZE/2), SCR_HEI - int(r*BLOCK_SIZE+BLOCK_SIZE/2)), RADIUS)

    #Every previous instruction was sent to the 'buffer',
    #The update() method refreshes the screen to display everything we have told it to display
    print(board)
    pygame.display.update()

def main():
#Create instance of pygame
    pygame.init()
#Initialize variables
    NUM_COLUMNS = 5
    NUM_ROWS = 3
    BLOCK_SIZE = 100
    RADIUS = int(BLOCK_SIZE/2 - 5)
    
    SCR_WID = NUM_COLUMNS * BLOCK_SIZE
    SCR_HEI = (NUM_ROWS+1)*BLOCK_SIZE
    size = (SCR_WID, SCR_HEI)
    turn = 0
    game_over = False
 #Set up display   
    board = create_board(NUM_ROWS, NUM_COLUMNS)
    screen = pygame.display.set_mode(size)
    draw_board(screen, board, NUM_ROWS, NUM_COLUMNS, BLOCK_SIZE, RADIUS, SCR_HEI)
    pygame.display.set_caption('Connect 4')
    game_font = pygame.font.SysFont('Arial', 75)
    
#The game loop
    while game_over == False:
        #References pygame's built-in 'event-queue' to compare and act based on the user input
        for event in pygame.event.get():
            if event.type == QUIT:
                #Quits the game if the user presses the red X in the corner of the screen, or ALT+F4
                pygame.quit()
                sys.exit()
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                #Note that any mouse button can be pressed down
                pygame.draw.rect(screen, COLORS[0], (0,0, SCR_WID, BLOCK_SIZE))
                # Get Player 1 input
                if turn == 0 :
                    posx = event.pos[0] #The X-coordinate of the mouse position
                    print(event.pos[0], event.pos[1])
                    col = int(math.floor(posx/BLOCK_SIZE)) #makes the column an integer value of the rounded down value of position X divided by 100, to have columns 0-6 instead of 000-699 for the X coordinates

                    #Compares where the mouse was when the mouse button was pressed down
                    if valid_move(board, col, NUM_ROWS):
                        row = valid_row(board, col, NUM_ROWS)
                        place_piece(board, row, col, 1)

                        if is_winning_move(board, 1, NUM_ROWS, NUM_COLUMNS):
                            #Creates a label for the player who won and prints it across the top of the screen in that player's color
                            label = game_font.render('Player 1 wins!!!!!', 1, COLORS[3])
                            screen.blit(label, (40, 10))
                            game_over = True #Game over is no longer false, exiting the game loop
                            
                 # Get Player 2 input                                    
                else:
                    posx = event.pos[0]
                    col = int(math.floor(posx/BLOCK_SIZE)) #makes the column an integer value of the rounded down value of position X divided by 100, to have columns 0-6 instead of 000-699 for the X coordinates
                    if valid_move(board, col, NUM_ROWS):
                            row = valid_row(board, col, NUM_ROWS)
                            place_piece(board, row, col, 2)
                            if is_winning_move(board, 2, NUM_ROWS, NUM_COLUMNS):
                                label = game_font.render('Player 2 wins!!!!!', 1, COLORS[2])
                                screen.blit(label, (40, 10))
                                game_over = True
                turn = turn + 1
                turn = turn%2 # resets the turns from 1 to 0
                draw_board(screen, board, NUM_ROWS, NUM_COLUMNS, BLOCK_SIZE, RADIUS, SCR_HEI)

main()

