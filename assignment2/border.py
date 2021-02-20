import numpy as np
from design import *
from colorama import Fore, Back, Style


class Board:
    """creating screen for game"""

    def __init__(self, row, column):
        self.__row = row

        self.__column = column
        self.__grid = np.zeros((HEIGHT+12, WIDTH+1), dtype='<U20')
      #  print(self.__grid)
        self.__grid[:] = ' '
        self.__score = 0
        self.__time = 120
        self.__life = 3
       # print(self.__grid)

    def borderdefine(self):
        for i in range(self.__column+1):
            self.__grid[10][i] = B_BLUE + '='+RESET
            self.__grid[self.__row][i] = B_BLUE+'='+RESET
        for i in range(10, self.__row):
            self.__grid[i][0] = self.__grid[i][1] = B_BLUE+'|'+RESET
            self.__grid[i][self.__column] = self.__grid[i][self.__column -
                                                           1] = B_BLUE+'|'+RESET

    def __show__(self):
        print("\n\n")
        # for i in range(10):
        #     print(RESET+"      ", end='')
        #     for j in range(self.column+1):
        #         print(B_BLUE+self.__grid[i][j], end='')
        #     print()
        print(F_BLUE+"        Score:", self.__score,
              "        Time Left:", self.__time, self.__column, "        Life Left:", self.__life, "\n\n\n")
        for i in range(10, self.__row+1):
            print(RESET+"      ", end='')
            for j in range(self.__column+1):
                print(F_GREEN+self.__grid[i][j], end='')
            #print('|', end='')
            print()

    def __bordercollision__(self, ball):
        x = ball.getx()
        y = ball.gety()
        f = 0
        if(x <= 1):
            ball.setxvelocity(-1*ball.getxvelocity())
            f = 1
        if(x >= self.__column-1):
            ball.setxvelocity(-1*ball.getxvelocity())
            f = 1
        if (y <= 10):
            ball.setyvelocity(-1*ball.getyvelocity())
            f = 1
        if(y >= self.__row-1):
            f = 2

        return f

    def getgrid(self):
        return self.__grid[:]

    def life(self):
        return self.__life

    def getcolumn(self):
        return self.__column

    def getrow(self):
        return self.__row

    def setlife(self):
        self.__life -= 1

    def setscore(self, value):
        self.__score = value

    def getscore(self):
        return self.__score
