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

COLOURS = {0: GREY,
           1: YELLOW,
           2: RED,
           3: GREEN,
           4: BLUE,
           5: PINK}

screen = pygame.display.set_mode(SIZE)

ball = pygame.image.load("ball.bmp")
ballrect = ball.get_rect()

screen.fill(GREY)

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    # ballrect = ballrect.move(speed)
    # if ballrect.left < 0 or ballrect.right > WIDTH:
    #     speed[0] = -speed[0]
    # if ballrect.top < 0 or ballrect.bottom > HEIGHT:
    #     speed[1] = -speed[1]

    # gameBoard = board.Board()
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

    # screen.blit(ball, ballrect)
    pygame.display.update()
    pygame.time.wait(50)
