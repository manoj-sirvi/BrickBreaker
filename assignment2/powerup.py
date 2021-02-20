from design import *
import time
array = ['@', '$', '%', '&', '*', ':']
color = [B_BLACK, B_BLUE, B_CYAN, B_RED, B_MIX, B_YELLOW]

POWER_TIME = 4


class item:
    def __init__(self, x, y, index, grid, row, column):
        self._y_velocity = -1
        self._x = x
        self._index = index
        self._y = y
        self._time = 0
        grid[y][x] = color[self._index] + array[self._index]+RESET
        # print("destroy", grid[y][x], y, x)

    def _move(self, grid, row, column):
        if((self._y > 10 and self._y < row-1) and (self._x > 2 and self._x < column-1) and grid[self._y][self._x] == color[self._index]+array[self._index]+RESET):
            grid[self._y][self._x] = ' '
        self._y += 1
        # print(grid[self._y][self._x] == ' ')
        if((self._y > 10 and self._y < row-1) and (self._x > 2 and self._x < column-1) and grid[self._y][self._x] == ' '):
            grid[self._y][self._x] = color[self._index] + \
                array[self._index]+RESET

    def _collision(self, padle_x, padle_y, row):
        if(self._y == row-2):
            if(padle_x <= self._x <= padle_y):
                return 1

        return 0

    def settime(self):
        if(self._activated == 0):
            self._time = time.time()
            self._activated = 1


class Size_increase(item):
    def __init__(self, x, y, index, grid, row, column):
        super().__init__(x, y, index, grid, row, column)
        self._activated = 0

    def _update(self, ball, grid, row, column, padle):
        pass

    def _Reset(self, ball, grid, row, column, padle):
        pass


class Size_decrease(item):
    def __init__(self, x, y, index, grid, row, column):
        super().__init__(x, y, index, grid, row, column)
        self._activated = 0
        self._increases = 1

    def _update(self, ball, grid, row, column, padle):
        if(self._activated == 0):
            self.settime()

    def _Reset(self, ball, grid, row, column, padle):
        pass


class fastball(item):
    def __init__(self, x, y, index, grid, row, column):
        super().__init__(x, y, index, grid, row, column)
        self._activated = 0
        self._increases = 2

    def _update(self, ball, grid, row, column, padle):
        if(ball._activated == 0):
            self.settime()
            ball._activated = 1
            # print("enter")
            if(ball.getxvelocity() >= 0):
                ball.setxvelocity(ball.getxvelocity()+self._increases)
            else:
                ball.setxvelocity(ball.getxvelocity()-self._increases)
            return 1

        return 0

    def _Reset(self, ball, grid, row, column, padle):
        if(time.time()-self._time > POWER_TIME):
            # print("\n\n\n", time.time()-self._time)
            ball._activated = 0
            if(ball.getxvelocity() >= 0):
                ball.setxvelocity(ball.getxvelocity()-self._increases)
            else:
                ball.setxvelocity(ball.getxvelocity()+self._increases)
            return 1
        return 0


class multipleball(item):
    pass


class Throughball(item):
    def __init__(self, x, y, index, grid, row, column):
        super().__init__(x, y, index, grid, row, column)
        self._activated = 0

    def _update(self, ball, grid, row, column, padle):
        if(ball._thball == 0):
            # self.settime()
            ball._thball = 1

    def _Reset(self, ball, grid, row, column, padle):
        if(time.time()-self._time > POWER_TIME):
            ball._thball = 0
        else:
            ball._thball = 1
