import sys
import pygame
import board

pygame.init()
gameBoard = board.Board()

SQUARE_SIZE = 20
THICKNESS = 2

COLS = 10
ROWS = 20

WIDTH = COLS*SQUARE_SIZE
HEIGHT = ROWS*SQUARE_SIZE

SIZE = WIDTH, HEIGHT
speed = [2, 2]

BLACK = 0, 0, 0
YELLOW = 255, 255, 0
RED = 255, 0, 0
GREEN = 0, 255, 0
BLUE = 0, 0, 255
PINK = 255, 0, 255
WHITE = 255, 255, 255
GREY = 128, 128, 128
CYAN = 0, 255, 255
ORANGE = 255, 165, 0

COLOURS = {0: GREY,
           1: YELLOW,
           2: RED,
           3: GREEN,
           4: BLUE,
           5: PINK,
           6: CYAN,
           7: ORANGE}

screen = pygame.display.set_mode(SIZE)

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    #refresh screen
    screen.fill(GREY)

    b = gameBoard.get()
    for y in range(0, HEIGHT, SQUARE_SIZE):
        for x in range(0, WIDTH, SQUARE_SIZE):

            row = int((y/HEIGHT)*ROWS)
            col = int((x/WIDTH)*COLS)
            currentColour = COLOURS[b[row][col]]

            if currentColour != GREY:
                pygame.draw.rect(screen, BLACK,(x,y,SQUARE_SIZE,SQUARE_SIZE), THICKNESS)

                pygame.draw.rect(screen,
                                 currentColour,
                                 (x+THICKNESS,y+THICKNESS,SQUARE_SIZE-THICKNESS,SQUARE_SIZE-THICKNESS),
                                 0)

    pygame.display.update()
    pygame.time.wait(1000)
    gameBoard.cleanRows()
