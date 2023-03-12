# Задача 10: На столе лежат n монеток.
# Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть,
# чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть

n = int(input("Введите кол-во монеток: "))
moneys = []
for i in range(n):
    money = int(input(f'money_{i+1}--> '))
    moneys.append(money)
# print(moneys)
len_0 = 0
len_1 = 0
for money in moneys:
    if money > 0:
        len_1 += 1
    else:
        len_0 += 1
# print (len_0)
# print (len_1)
if len_1 > len_0:
    print(len_0)
else:
    print(len_1)
