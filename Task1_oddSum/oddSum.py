import classAdd

initClear = classAdd.InitSets()
work = classAdd.ExecModule()
work.CreatList()
work.FindOddSum()
print(f"Созданный список: {work.myList}")
print(f"Сумма нечетных индексов равна = {work.sumOdd}")
