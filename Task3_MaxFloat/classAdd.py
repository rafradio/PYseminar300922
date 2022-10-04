import os
import random

class InitSets:
    def __init__(this):
        clear = lambda: os.system("CLS")
        clear()

class ExecModule:
    def __init__(this):
        this.myLen = random.randrange(8, 15)
        this.minArray, this.maxArray = 0, 100
        this.myList = []

    def CreatList(this):
        for i in range(this.myLen):
            floatNumber = round(random.random() * 10, 2)
            this.myList.append(floatNumber)

    def CreatFloatList(this):
        this.myFloatList = []
        for i in range(this.myLen):
            float = round(this.myList[i] - int(this.myList[i]), 2)
            this.myFloatList.append(float)

    def MaxMinFloat(this):
        maxFloat = this.myFloatList[0]
        minFloat = this.myFloatList[0]
        for i in range(this.myLen):
            if (this.myFloatList[i] > maxFloat): maxFloat = this.myFloatList[i]
            else: 
                if (this.myFloatList[i] < minFloat): minFloat = this.myFloatList[i]

        print(f"Разница равна = {maxFloat - minFloat}")
