import random
class Board():

    def __init__(self):
        self.__BLANK = 0
        self.__board = [[self.__BLANK for x in range(10)] for y in range(20)]

        for x in range(10):
            for y in range(20):
                self.__board[y][x] = random.randrange(0, 6)

    def get(self):
        return self.__board
