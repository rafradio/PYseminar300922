import os
import random

class InitSets:
    def __init__(this):
        clear = lambda: os.system("CLS")
        clear()

class ExecModule:
    def __init__(this):
        this.myLen = random.randrange(5, 10)
        this.minArray, this.maxArray = 0, 100
        this.myList = []

    def CreatList(this):
        for i in range(this.myLen):
            this.myList.append(random.randrange(this.minArray, this.maxArray))
        
    def FindOddSum(this):
        this.sumOdd = 0
        for i in range(1, this.myLen, 2):
            this.sumOdd += this.myList[i]
