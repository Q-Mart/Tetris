import random
class Board():

    def __init__(self):
        self.__BLANK = 0
        self.__data = [[self.__BLANK for x in range(10)] for y in range(24)]

        for x in range(10):
            self.__data[23][x] = 1

            if x%2 == 0:
                self.__data[22][x] = 2

    def __getColour(self):
        return random.randrange(0,6)

    def get(self):
        return self.__data[4:]

    def cleanRows(self):
        # check if a row is full, deletes it and shifts above rows down
        for y in range(23, 1, -1):
            full = True
            for x in range(10):
                if self.__data[y][x] == self.__BLANK:
                    full = False

            if full:
                # delete the row
                for x in range(10):
                    self.__data[y][x] = self.__BLANK

                # shift all rows above down
                currentRow = y
                while currentRow != 0:
                    aboveRow =  currentRow - 1
                    for x in range(10):
                        self.__data[currentRow][x] = self.__data[aboveRow][x]

                    currentRow -= 1
