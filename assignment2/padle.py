from design import *


class Padle:
    def __init__(self, grid, row, column):
        self.__x1 = 57
        self.__x2 = 71
        # self.padles = "======="
        # grid[row-4] = row-4
        # grid[row-3] = 2
        # grid[28] = 'p'
        for i in range(2, column-2):
            if i >= self.__x1 and i <= self.__x2:
                grid[row-1][i] = B_BLACK+"="+RESET
            else:
                grid[row-1][i] = ' '

    def moveright(self, grid, row, column):
        # print(self.__x2, column-3)
        # print(grid[row-1][column-2])
        if(self.__x2 < column-2):
            self.__x1 = max(3, self.__x1+3)
            self.__x2 = min(119, self.__x2+3)
            self.__x1 = self.__x2-14

            for i in range(2, column-2):
                if i >= self.__x1 and i <= self.__x2:
                    grid[row-1][i] = B_BLACK+"="+RESET
                else:
                    grid[row-1][i] = ' '

    def moveleft(self, grid, row, column):
        if(self.__x1 > 2):
            self.__x1 = max(2, self.__x1-3)
            self.__x2 = min(119, self.__x2-3)
            self.__x2 = self.__x1+14

            for i in range(2, column-2):
                if i >= self.__x1 and i <= self.__x2:
                    grid[row-1][i] = B_BLACK+"="+RESET
                else:
                    grid[row-1][i] = ' '

    def __padlecollision__(self, ball):
        if(ball.gety() == 48):

            if(ball.getx() >= self.__x1 and ball.getx() <= self.__x2):

                cn = (self.__x1+self.__x2)/2
                # print(self.__x1, self.__x2)
              #  print("hello", cn, int(ball.x))
                # ball.x_velocity += int(ball.getx()-cn)
                p = ball.getx()
                ball.setxvelocity(ball.getxvelocity()+int(int(p-cn)))
                # ball.y_velocity *= -1
                ball.setyvelocity(-1*ball.getyvelocity())
                # print(cn)
                # print((self.__x1+self.__x2)/2, p,
                #       ball.getxvelocity(), ball.getyvelocity())

    def moverightboth(self, ball, grid, row, column):

        if(self.__x2 < column-2):
            grid[ball.gety()][ball.getx()] = ' '
            a = self.__x2-ball.getx()
            self.__x1 = max(3, self.__x1+3)
            self.__x2 = min(119, self.__x2+3)
            self.__x1 = self.__x2-15

            for i in range(2, column-2):
                if i >= self.__x1 and i <= self.__x2:
                    grid[row-1][i] = B_BLACK+"="+RESET
                else:
                    grid[row-1][i] = ' '

            ball.setx(self.__x2-a)
            # print(grid[row-1][64])
            grid[ball.gety()][ball.getx()] = 'o'

    def moveleftboth(self, ball, grid, row, column):
        if(self.__x1 > 2):
            grid[ball.gety()][ball.getx()] = ' '
            a = ball.getx()-self.__x1
            self.__x1 = max(2, self.__x1-3)
            self.__x2 = min(119, self.__x2-3)
            self.__x2 = self.__x1+15

            for i in range(2, column-2):
                if i >= self.__x1 and i <= self.__x2:
                    grid[row-1][i] = B_BLACK+"="+RESET
                else:
                    grid[row-1][i] = ' '
            ball.setx(self.__x1+a)
            grid[ball.gety()][ball.getx()] = 'o'

    def setx1(self, value):
        self.__x1 = value

    def setx2(self, value):
        self.__x2 = value

    def getx1(self):
        return self.__x1

    def getx2(self):
        return self.__x2
