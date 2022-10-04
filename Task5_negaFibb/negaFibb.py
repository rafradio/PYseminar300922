import classAdd

initClear = classAdd.InitSets()
work = classAdd.ExecModule()
work.CreatArray()

print(f"Созданный список: {work.array}")
print(f"Сумма итераций равна = {work.counter}")