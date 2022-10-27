#  Реализуйте алгоритм перемешивания списка. Без функции shuffle из модуля random.

import random
n=10
spisok = [item for item in range(0, n)]

print(spisok)

for i in range(len(spisok)):
    j=random.randint(0,len(spisok)-1)
    temp=spisok[i]   
    spisok[i]=spisok[j]
    spisok[j]=temp 

print(spisok)