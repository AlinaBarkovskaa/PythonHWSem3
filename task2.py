# Требуется найти в массиве A[1..N] самый близкий повеличине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. В
# последующих строках записаны N целых чисел Ai. Последняя строка
# содержит число X
# 1 2 3 4 5
# 6 -> 5

numbers = int(input('Введите numbers: ')) 
list_numbers = [int(input('Введите n: ')) for _ in range(numbers)]
x = int(input('Введите x: '))
b=[abs(list_numbers[i]-x) for i in range(len(list_numbers))]
print(list_numbers[b.index(min(b))])
