import os
import random

class InitSets:
    def __init__(this):
        clear = lambda: os.system("CLS")
        clear()

class ExecModule:
    def __init__(this):
        this.myLen = random.randrange(8, 14)
        this.mapArray = {
            -2: -1,
            -1: 1,
            0: 0,
            1: 1,
            2: 1
        }
        this.array = []
        this.counter = 0

        print(this.myLen)

    def CreatArray(this):

        for i in range(-this.myLen, this.myLen + 1):
            this.array.append(this.FindFibb(i))

    def FindFibb(this, keyNum):
        this.counter += 1

        if keyNum in this.mapArray.keys():
            return this.mapArray[keyNum]

        if keyNum > 0: res = this.FindFibb(keyNum - 1) + this.FindFibb(keyNum - 2)
        else: res =  -this.FindFibb(keyNum + 1) + this.FindFibb(keyNum + 2)

        this.mapArray[keyNum] = res

        return res

   