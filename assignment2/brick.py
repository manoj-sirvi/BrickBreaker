
import border
from design import *
import random
import sys
from powerup import *
array = ['@', '$', '%', '&', '*', ':']
color = [B_BLACK, B_BLUE, B_CYAN, B_RED, B_MIX, B_YELLOW]
tree = [[0], [0], [0], [0], [0], [0], [0]]
special1 = []
powerup_array = []
Score = [0]
Hello = [Throughball, Throughball, Throughball, Throughball, Throughball,
         Throughball]


class Brick:
    def __init__(self, x1, y1):
        self._x1 = x1
        self._x2 = x1+5
        self._y1 = y1
        self._y2 = y1+2
        self._visible = 1

    def collisiongrid(self, grid, row, column):
        print("wdkuwe")


class Breakable(Brick):
    def __init__(self, x1, y1):
        super().__init__(x1, y1)
        self._power = random.randint(1, 6)
        self._special = 0

    def _assign(self, grid, row, column):
        # print(self._power)
        if(self._power <= 0):
            grid[self._y1:self._y2, self._x1:self._x2][:] = ' '
            a = random.randint(0, 5)
            powerup_array.append(
                Hello[a](self._x1+2, self._y1+1, a, grid, row, column))
            # print(";hello")

        if(self._power <= 2 and self._power > 0):
            grid[self._y1:self._y2, self._x1:self._x2][:] = B_MAGENTA + \
                str(self._power)+RESET

        if(self._power >= 3 and self._power <= 4):
            grid[self._y1:self._y2, self._x1:self._x2][:] = B_CYAN + \
                str(self._power)+RESET

        if(self._power <= 6 and self._power > 4):
            grid[self._y1:self._y2, self._x1:self._x2][:] = B_RED + \
                str(self._power)+RESET

    def _collision(self, ball, grid, row, column, value):
        if(value):
            self._power = 0
        else:
            self._power -= 1
        if(self._power <= 0):
            Score[0] += 1
            try:
                breakable.remove(self)
                a = random.randint(0, 5)
                powerup_array.append(
                    Hello[a](self._x1+2, self._y1+1, a, grid, row, column))
                # print(";hello")
            except:
                pass
            grid[self._y1:self._y2, self._x1:self._x2][:] = ' '
            flag = 1
        else:
            self._assign(grid, row, column)
            Score[0] += self._power+1
        # print("ended")


class UnBreakable(Brick):
    def __init__(self, x1, y1):
        super().__init__(x1, y1)
        self._power = -1
        self._special = 0

    def _assign(self, grid, row, column):
        if(self._power == 0):
            grid[self._y1:self._y2, self._x1:self._x2][:] = ' '
        else:
            grid[self._y1:self._y2, self._x1:self._x2][:] = B_LIGHTYELLOW + \
                'U'+RESET

    def _collision(self, ball, grid, row, column, value):
        if(value):
            self._power = 0
        self._power -= 0
        self._assign(grid, row, column)


class Bonus(Brick):
    def __init__(self, x1, y1):
        super().__init__(x1, y1)
        self._power = -2
        self._special = 1

    def _assign(self, grid, row, column):
        check = random.randint(0, 2)
        if(self._power == 0):
            grid[self._y1:self._y2, self._x1:self._x2][:] = ' '

        else:
            grid[self._y1:self._y2, self._x1:self._x2][:] = color[check % 2] + \
                'E'+RESET

    def _collision(self, ball, grid, row, column, value):
        self._power -= 0
        current = []
        current.append(self)
        f = 1
        i = 0
        counter = 0
        while (i < len(current)):
            i = current[i]
            i._power = 0

            for k in list(breakable):
                if((i._x1 == k._x2 and i._y1 == k._y1) or (i._x2 == k._x1 and i._y1 == k._y1) or (i._y1 == k._y2 and i._x1 == k._x1) or (i._y2 == k._y1 and i._x1 == k._x1) or (i._x1 == k._x1 and i._y1 == k._y1) or
                   (i._x1 == k._x2 and i._y1 == k._y2) or (i._x2 == k._x1 and i._y1 == k._y2) or (k._x2 == i._x1 and i._y2 == k._y1) or (i._y2 == k._y1 and i._x2 == k._x1)):
                    if(k._special and (i._x1 == k._x1 and i._y1 == k._y1) == 0):
                        current.append(k)
                    else:
                        # print("yes")
                        if(k._power >= 0):
                            Score[0] += k._power
                        k._power = 0
                        try:
                            breakable.remove(k)
                        except:
                            pass
                        k._assign(grid, row, column)
                        # tree[counter].append({k._y1, k._y2, i._y1, i._y2})
            # i._assign(grid, row, column)
            current.remove(i)
            i._special = 0
            i = 0

            # print(current, i)
            # if(counter == 1):
            #    print(grid[:])
            # print(breakable)
            #    border._
            # quit()
            counter += 1
    # sys.exit()


class colorBrick(Breakable):
    pass


breakable = []
unbreakable = []
expoled = []


def Create_Brick(obj):
    for i in range(6):
        test = Bonus(50+5*i, 30)
        test._assign(obj.getgrid(), obj.getrow(), obj.getcolumn())
        breakable.append(test)
    for i in range(4):
        test = Breakable(55+5*i, 28)
        test._assign(obj.getgrid(), obj.getrow(), obj.getcolumn())
        breakable.append(test)
    for i in range(3):
        test = Breakable(60+5*i, 26)
        test._assign(obj.getgrid(), obj.getrow(), obj.getcolumn())
        breakable.append(test)
    for i in range(2):
        test = Breakable(50+5*i, 32)
        test._assign(obj.getgrid(), obj.getrow(), obj.getcolumn())
        breakable.append(test)
    for i in range(2):
        test = Breakable(65+5*i, 32)
        test._assign(obj.getgrid(), obj.getrow(), obj.getcolumn())
        breakable.append(test)
    for i in range(1):
        test = UnBreakable(60, 32)
        test._assign(obj.getgrid(), obj.getrow(), obj.getcolumn())
        breakable.append(test)
    for i in range(1):
        test = Breakable(55, 34)
        test._assign(obj.getgrid(), obj.getrow(), obj.getcolumn())
        breakable.append(test)
    for i in range(1):
        test = UnBreakable(65, 34)
        test._assign(obj.getgrid(), obj.getrow(), obj.getcolumn())
        breakable.append(test)
    for i in range(3):
        test = Breakable(45, 28+2*i)
        test._assign(obj.getgrid(), obj.getrow(), obj.getcolumn())
        breakable.append(test)
    # special1 = breakable
    # print(special1)
    # for i in range(1):
    #     test = Breakable(69, 44)
    #     test._assign(obj.getgrid(), obj.getrow(), obj.getcolumn())
    #     breakable.append(test)
