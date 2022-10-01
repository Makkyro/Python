# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).

# Пример:
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

flag = True
while flag:
    cord = input('Введите два числа через пробел:').split()
    if len(cord) == 2:
        x, y = int(cord[0]), int(cord[1])
        if x == 0 or y == 0:
            print('Числа должны быть больше 0')
        else:
            flag = not flag
if x > 0:
    if y > 0:
        print('1')
    else:
        print('4')
if x < 0:
    if y > 0:
        print('2')
    else:
        print('3')