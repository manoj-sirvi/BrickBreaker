from design import *
import random
from brick import *
import itertools


class Ball:

    def __init__(self, grid, row, column):
        index = random.randint(57, 71)
        self._y = row-2
        self._x = 64
        self._y_velocity = -2
        self._activated = 0
        self._thball = 0

        self._x_velocity = 0
        if((self._y > 10 and self._y < row-1) and (self._x > 2 and self._x < column-1)):
            grid[self._y][self._x] = 'o'

    @staticmethod
    def collinear(x1, y1, x2, y2, x3, y3):
        """ Calculation the area of
        triangle. We have skipped
        multiplication with 0.5 to
        avoid floating point computations """
        a = x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)
        if (a == 0):
            return 1
        else:
            return 0

    @staticmethod
    def positive_negative(x):
        if(x > 0):
            return 1
        else:
            if(x == 0):
                return 0
            else:
                return -1

    def move(self, grid, row, column, f):
        if((self._y > 10 and self._y < row-1) and (self._x > 2 and self._x < column-1)):
            grid[self._y][self._x] = ' '

        x_predicted = self._x+int(self._x_velocity*0.5)
        y_predicted = self._y-int(self._y_velocity*0.5)

        f1 = self.positive_negative(self._x_velocity)
        f2 = self.positive_negative(self._y_velocity)
        a = self._x
        b = self._y
        f = 0
        arr = []

        # print()

        # print(self._x_velocity, self._y_velocity, self._x,
        #       x_predicted, self._y, y_predicted, f1, f2)
        # print(k._x1, k._x2, k._y1, k._y2)
        if(f1 == 0):
            for k in (breakable):
                if((y_predicted == k._y1+1 or y_predicted == k._y1) and k._x1 <= self._x < k._x2):
                    k._collision(self, grid, row, column, self._thball)
                    f = 1
                    if(self._thball == 0):
                        self._y_velocity *= -1
                    break

        else:
            k1 = int(abs(x_predicted-self._x)/2)+self._x
            for i in range(self._x, x_predicted+f1, f1):
                # arr.append({i})
                # arr.append(i)
                # arr.append(self._x)
                # arr.append(self._y)
                # arr.append(i)
                for k in list(breakable):
                    a = k1
                    if(f1 == 1 and f2 == 1):
                        if(i <= a):
                            if(k._y2 == self._y and k._x1 <= i < k._x2):
                                k._collision(self, grid, row,
                                             column, self._thball)
                                if(self._thball == 0):
                                    self._y_velocity *= -1
                                self._x = i
                                self._y = k._y2
                                f = 1
                            if((k._y2-1 == self._y or k._y1 == self._y) and k._x1-1 == i):
                                k._collision(self, grid, row,
                                             column, self._thball)
                                if(self._thball == 0):
                                    self._x_velocity *= -1
                                self._x = i
                                f = 1
                        else:
                            if(k._y2 == self._y+1 and k._x1 <= i < k._x2):
                                k._collision(self, grid, row,
                                             column, self._thball)
                                if(self._thball == 0):
                                    self._y_velocity *= -1
                                self._x = i
                                self._y = k._y2
                                f = 1
                            if((k._y2-1 == self._y+1 or k._y1 == self._y+1) and k._x1-1 == i):
                                k._collision(self, grid, row,
                                             column, self._thball)
                                if(self._thball == 0):
                                    self._x_velocity *= -1
                                self._x = i
                                self._y -= 1
                                f = 1
                    if(f1 == 1 and f2 == -1):
                        if(i <= a):
                            # print((k._y1+1 == self._y or k._y1 == self._y))
                            if((k._y1 == self._y+1 or k._y1 == self._y) and k._x1-1 == i):
                                k._collision(self, grid, row,
                                             column, self._thball)
                                if(self._thball == 0):
                                    self._x_velocity *= -1
                                self._x = i
                                f = 1
                                # arr.append(2)
                            if(k._y1-1 == self._y and k._x1 <= i < k._x2):
                                k._collision(self, grid, row,
                                             column, self._thball)
                                if(self._thball == 0):
                                    self._y_velocity *= -1
                                self._x = i
                                f = 1
                                # arr.append(3)
                        else:
                            if((k._y1 == self._y or k._y1 == self._y+1) and k._x1-1 == i):
                                k._collision(self, grid, row,
                                             column, self._thball)
                                if(self._thball == 0):
                                    self._x_velocity *= -1
                                self._x = i
                                # self._y += 1
                                f = 1
                                # arr.append(4)
                            if(k._y1-1 == self._y+1 and k._x1 <= i < k._x2):
                                # arr.append(k._power)
                                k._collision(self, grid, row,
                                             column, self._thball)
                                # arr.append(self._x)
                                # arr.append(self._y)
                                # arr.append(k._y1)
                                # arr.append(i)
                                # arr.append(k._x1)
                                # arr.append(a)
                                if(self._thball == 0):
                                    self._y_velocity *= -1
                                self._x = i
                                # self._y += 1
                                f = 1

                    if(f1 == -1 and f2 == 1):
                        k1 = x_predicted+int((x_predicted-self._x)/2)
                        if(i >= a):
                            if((self._y == k._y1 or k._y1+1 == self._y) and k._x2 == i):
                                k._collision(self, grid, row,
                                             column, self._thball)
                                if(self._thball == 0):
                                    self._x_velocity *= -1
                                self._x = i
                                f = 1
                            if(k._y1+1 == self._y-1 and k._x1 <= i < k._x2):
                                k._collision(self, grid, row,
                                             column, self._thball)
                                if(self._thball == 0):
                                    self._y_velocity *= -1
                                self._x = i
                                f = 1
                        else:
                            if(k._y2 == self._y-1 and k._x1 <= i < k._x2):
                                k._collision(self, grid, row,
                                             column, self._thball)
                                if(self._thball == 0):
                                    self._y_velocity *= -1
                                self._x = i
                                self._y -= 1
                                f = 1
                            if((self._y-1 == k._y1 or self._y-1 == k._y1+1) and k._x2 == i):
                                k._collision(self, grid, row,
                                             column, self._thball)
                                if(self._thball == 0):
                                    self._x_velocity *= -1
                                self._x = i
                                self._y -= 1
                                f = 1
                    if(f1 == -1 and f2 == -1):
                        k1 = x_predicted+int((x_predicted-self._x)/2)
                        if(i >= a):
                            if(self._y+1 == k._y1 and k._x1 <= i < k._x2):
                                k._collision(self, grid, row,
                                             column, self._thball)
                                if(self._thball == 0):
                                    self._y_velocity *= -1
                                self._x = i
                                f = 1
                            if((self._y == k._y1 or self._y == k._y1+1) and k._x2 == i):
                                k._collision(self, grid, row,
                                             column, self._thball)
                                if(self._thball == 0):
                                    self._x_velocity *= -1
                                self._x = i
                                f = 1
                        else:
                            if((self._y+1 == k._y1 or self._y+1 == k._y1+1) and k._x2 == i):
                                k._collision(self, grid, row,
                                             column, self._thball)
                                if(self._thball == 0):
                                    self._x_velocity *= -1
                                self._x = i
                                self._y += 1
                                f = 1
                            if(self._y+1 == k._y1-1 and k._x1 <= i < k._x2):
                                k._collision(self, grid, row,
                                             column, self._thball)
                                if(self._thball == 0):
                                    self._y_velocity *= -1
                                self._x = i
                                self._y += 1
                                f = 1

                                # a = k1
                                # if(f1 ):
                                #     if(i <= a):
                                #         if(k._x1 <= i <= k._x2 and ((k._y2-1 == self._y and f2 == 1) or (k._y1-1 == self._y and f2 == -1))):

                                #             k._collision(self, grid, row, ,column,self._thball)
                                #             self._y_velocity *= -1
                                #             self._x = i
                                #             f = 1
                                #             arr.append(i)
                                #             print("a")
                                #             break

                                #     else:
                                #         if(k._x1-1 <= i <= k._x2 and ((k._y2-1 == self._y and f2 == 1) or (k._y1-1 == self._y and f2 == -1))):

                                #             k._collision(self, grid, row, column)
                                #             self._x_velocity *= -1
                                #             self._x = i
                                #             # self._y = y_predicted
                                #             f = 1
                                #             if((k._y2 == self._y+1 and f2 == 1)):
                                #                 self._y = k._y2-1
                                #             arr.append(i)
                                #             arr.append(0)
                                #             print("sec", k._x1, k._x2, i, self._y, k._y1)
                                #             break
                                # else:
                                #     k1 = -int(abs(x_predicted-self._x)/2)+self._x
                                #     a = k1
                                #     # print(self._x, self._y, a, k._x1, k._x2, k._y1, k._y2)
                                #     if(i >= a):
                                #         if(k._x1 <= i <= k._x2 and ((k._y2-1 == self._y and f2 == 1) or (k._y1-1 == self._y and f2 == -1))):

                                #             k._collision(self, grid, row, column)
                                #             self._y_velocity *= -1
                                #             self._x = i
                                #             f = 1
                                #             print("th", k._x1, k._x2)
                                #             break

                                #     else:
                                #         # print((k._y2 == self._y+1 and f2 == 1),
                                #         #   k._x1-1 <= i <= k._x2+1, self._x, self._y, a, k._x1, k._x2, k._y1, k._y2)
                                #         if(k._x1-1 <= i <= k._x2 and ((k._y2-1 == self._y and f2 == 1) or (k._y1-1 == self._y and f2 == -1))):

                                #             k._collision(self, grid, row, column)
                                #             self._x_velocity *= -1
                                #             self._x = i
                                #             if((k._y2 == self._y+1 and f2 == 1)):
                                #                 self._y = k._y2-1
                                #                 print("hello ")
                                #                 # self._y =
                                #             f = 1
                                #             print("fo", k._x1, k._x2, self._y, k._y1)
                                #             arr.append(i)
                                #             arr.append(0)
                                #             break
                if(f):
                    arr.append(1)
                    # print("breaking yes")
                    break
            # if(((abs(i-k._x1) == 2) or (abs(i-k._x2) == 2)) and ((abs(j-k._y1) == 2) or (abs(j-k._y2) == 2))):
            #     self._x_velocity *= -1
            #     self._y_velocity *= -1
            #     self._x = i
            #     self._y = j
            #     k._collision(self, grid, row, column)
            #     f = 1
            #     print(k._x1, k._x2, k._y1, k._y2)
            # break
            # else:
            # if(((abs(i-k._x1) < 1) or (abs(i-k._x2) < 1)) and (k._y1 <= j < k._y2)):
            #     self._x_velocity *= -1
            #     # k._collision(self, grid, row, column)
            #     # f = 1
            #     self._x = i
            #     self._y = j
            # print("first", k._x1, k._x2, k._y1, k._y2)
            # break

            # if((abs(j-k._y1) < 1) or (abs(j-k._y2) < 1) and (k._x1 <= i < k._x2)):
            #     self._y_velocity *= -1
            #     # k._collision(self, grid, row, column)
            #     self._x = i
            #     self._y = j
            # print("second", k._x1, k._x2, k._y1, k._y2, i, j, f1, -f2)
            # f = 1
            # break

        if(f == 0):
            self._x = x_predicted
            self._y = y_predicted
            # pass

            # print(self.x, self.y)
        if((self._y > 10 and self._y < row-1) and (self._x > 2 and self._x < column-1)):
            grid[self._y][self._x] = 'o'
        return arr

    def reversexvelocity(self):
        self._x_velocity = -1*self._x_velocity

    def __repr__(self):
        return "%d %d %d %d" % (self._x, self._y, self._x_velocity, self._y_velocity)

    def getx(self):
        return (self._x)

    def gety(self):
        return self._y

    def setx(self, value):
        self._x = value

    def sety(self, value):
        self._y = value

    def getxvelocity(self):
        return self._x_velocity

    def getyvelocity(self):
        return self._y_velocity

    def setxvelocity(self, value):
        self._x_velocity = value

    def setyvelocity(self, value):
        self._y_velocity = value


class NewBall(Ball):
    def __init__(self, ball):
        # print(super().getx(ball))
        self._y = ball.gety()
        self._x = ball.getx()
        self._x_velocity = -1*ball.getxvelocity()
        self._y_velocity = -1*ball.getyvelocity()
        # print(self._x, self._y)
