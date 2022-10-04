import classAdd

initClear = classAdd.InitSets()
work = classAdd.ExecModule()
work.CreatList()
work.CreatFloatList()
print(f"Созданный список: {work.myList}")
print(f"Дробная часть = {work.myFloatList}")
work.MaxMinFloat()
