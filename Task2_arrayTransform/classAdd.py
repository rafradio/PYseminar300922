import os
import random

class InitSets:
    def __init__(this):
        clear = lambda: os.system("CLS")
        clear()

class ExecModule:
    def __init__(this):
        this.myLen = random.randrange(5, 10)
        this.minArray, this.maxArray = 1, 10
        this.myList = []
        this.myNewList = []

    def CreatList(this):
        for i in range(this.myLen):
            this.myList.append(random.randrange(this.minArray, this.maxArray))

    def FindNewArray(this):
        for i in range(this.myLen // 2):
            this.myNewList.append(this.myList[i] * this.myList[this.myLen - 1 - i])
        if this.myLen % 2 == 1: this.myNewList.append(this.myList[i + 1] ** 2)