# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

def user_input():
    num = input('Введите число: ')
    while not num.isdigit():
        num = input('Введите число: ')
    return int(num)

print(f'{user_input():b}')