import random

class ShapeGenerator():

    def __init__(self):
        L = [[0,1,0],
             [0,1,0],
             [0,1,1]]

        J = [[0,2,0],
             [0,2,0],
             [2,2,0]]

        I = [3,3,3,3]

        O = [[4,4],
             [4,4]]

        S = [[0,0,5,5],
             [5,5,0,0]]

        T = [[6,6,6],
             [0,6,0]]

        Z = [[7,7,0,0],
             [0,0,7,7]]

        self.__shapes = [L, J, I, O, S, T, Z]

    def __rotate(self, l):
        return list(zip(*l[::-1]))

    def getShape(self):
        numShapes = len(self.__shapes)
        randomIndex = random.randrange(0, numShapes)
        shape = self.__shapes(randomIndex)

        # randomly rotate it
        for i in range(random.randrange(4)):
            shape = self.__rotate(shape)

        return shape
