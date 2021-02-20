from border import *
from design import *
from padle import *
from input import *
from ball import *
import time
from brick import *

obj = Board(HEIGHT, WIDTH)
obj.borderdefine()
fl1 = 0


ball = []
grid = obj.getgrid()
getch = Get()
obj1 = Padle(obj.getgrid(), obj.getrow(), obj.getcolumn())
k = Ball(obj.getgrid(), obj.getrow(), obj.getcolumn())
ball.append(k)
observe = []
Create_Brick(obj)
start = 0
# print(breakable)
# exit(0)
re = 0
tracker = time.time()
start = time.time()
arr = []
arr1 = []
counter = 0

while True and obj.life():

    # counter += 1

    if time.time()-tracker >= 0.10:
        tracker = time.time()

        inputdata = input_to(getch)
        print("\033[%d;%dH" % (0, 0))
        obj.setscore(int(Score[0]))
        obj.__show__()

        arr1.append(inputdata)
        if(fl1 == 0):
            if(inputdata == 'd'):
                obj1.moverightboth(
                    ball[0], obj.getgrid(), obj.getrow(), obj.getcolumn())
            if(inputdata == 'a'):
                obj1.moveleftboth(ball[0], obj.getgrid(),
                                  obj.getrow(), obj.getcolumn())
       # print(inputdata)
        if(inputdata == 'd' and fl1):
            obj1.moveright(obj.getgrid(), obj.getrow(), obj.getcolumn())
            # arr.append(inputdata)
        if(inputdata == 'a' and fl1):
            obj1.moveleft(obj.getgrid(), obj.getrow(), obj.getcolumn())
            # arr.append(inputdata)
        # print(len(powerup_array), len(observe))
        for i in list(powerup_array):
            if(counter):

                i._move(obj.getgrid(), obj.getrow(), obj.getcolumn())
                if (i._collision(obj1.getx1(), obj1.getx2(), obj.getrow())):
                    observe.append(i)
                    # try:
                    #     powerup_array.remove(i)
                    # except:
                    #     pass
                if(i._y >= obj.getrow()-1):
                    try:
                        powerup_array.remove(i)
                    except:
                        pass

        if(inputdata == 'q'):
            # print(powerup_array)

            break
        counter += 1
        counter %= 2
        # if(inputdata == 't' and fl1):
        # print("hello,hii")
        for j in list(observe):
            # if(j._index == 1):
            #     observe.remove(j)
            #     vitual = []
            #     for i in range(len(ball)):
            #         # obj2 = ball[i]
            #         # print("heelo1", obj2.x_velocity)
            #         # obj2.reversexvelocity()
            #         vitual.append(NewBall(ball[i]))
            #         # print("heelo", obj2.x_velocity)
            #     ball = ball+vitual
            # else:
            # j.settime()
            op = 0
            if(j._activated == 0):
                j.settime()
            for i in list(ball):
                lo = j._update(i, obj.getgrid(), obj.getrow(),
                               obj.getcolumn(), obj1)

                # print(i.getxvelocity(), i.getyvelocity())
                op = j._Reset(i, obj.getgrid(), obj.getrow(),
                              obj.getcolumn(), obj1)
                print(i._thball)
                # print(i.getxvelocity(), i.getyvelocity())
            if(op):
                observe.remove(j)

        if(fl1):
            # print("hello")
            # print(ball[0].getxvelocity(), ball[0].getyvelocity())
            for i in list((ball)):
                re = obj.__bordercollision__(i)
                obj1.__padlecollision__(i)

                if(re == 2):
                    ball.remove(i)
                    if(len(ball) < 1):
                        observe.clear()
                        for j in list(powerup_array):
                            grid[j._y][j._x] = ' '
                        powerup_array.clear()
                        obj.setlife()
                        ball.append(
                            Ball(obj.getgrid(), obj.getrow(), obj.getcolumn()))
                        obj1 = Padle(obj.getgrid(), obj.getrow(),
                                     obj.getcolumn())
                        fl1 = 0
                else:
                    # print("hsdsgd")
                    p = i.move(obj.getgrid(), obj.getrow(),
                               obj.getcolumn(), re)
                    # fl1 = 0

        if(inputdata == ' '):
            fl1 = 1
