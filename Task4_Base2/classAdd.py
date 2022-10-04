import os
import random

class InitSets:
    def __init__(this):
        clear = lambda: os.system("CLS")
        clear()

class ExecModule:
    def __init__(this):
        this.myNumber = random.randrange(45, 46)
        this.base2 = ""

    def ConvertBase2(this):
        while this.myNumber > 0:
            this.base2 = str(this.myNumber % 2) + this.base2
            this.myNumber = this.myNumber // 2
