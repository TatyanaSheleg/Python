# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# *Пример:*
# 5
#     1 2 3 4 5
#     6
#     -> 5

n=int (input ("введите кол-во элементов в массиве: "))

list=[]

for i in range (n):
    list.append(i+1)

print (list)

x=int (input ("введите число: "))

arr = list(map(int, input().split()))
x = int(input())
 
# eps = x
# result = arr[0]
# for i in arr:
#     if abs(i - x) < eps:
#         eps = abs(i - x)
#         result = i
# print(result)

# for i in list:
#     if list[i]<=x:   
# print(list [i])