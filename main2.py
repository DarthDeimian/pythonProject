
#2.
#Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.
#Примеры:
#
#- 1, 4, 8, 7, 5 -> 8
#- 78, 55, 36, 90, 2 -> 90

list = []
i = 0
while i < 5:
    j = int(input('Введите число: '))
    list.append(j)
    i+=1

print(list)

max = list[0]
i = 1
while i < len(list):
    if list[i] > max:
        max = list[i]
        i+=1
print(max)