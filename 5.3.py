x = int(input("Введите минимальную сумму инвестиций: "))
a = int(input("Введите сумму Майкла: "))
b = int(input("Введите сумму Ивана: "))
if (a >= x) and (b >= x):
    print(2)
elif a >= x:
    print("Mike")
elif b >= x:
    print("Ivan")
elif a + b >= x:
    print(1)
else:
    print(0)