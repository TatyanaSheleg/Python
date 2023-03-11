# Задача 6: Вы пользуетесь общественным транспортом?
# Вероятно, вы расплачивались за проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером,
# где сумма первых трех цифр равна сумме последних трех.
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
# Вам требуется написать программу, которая проверяет счастливость билета.
# *Пример:*
# 385916 -> yes
# 123456 -> no

a = int(input('Введите шестизначный номер билета: '))
summa1 = 0
while a > 999:
    x = a % 10
    summa1 = summa1+x
    a = a//10

summa2 = 0
while a > 0:
    x = a % 10
    summa2 = summa2+x
    a = a//10

b = summa1 == summa2
if b == True:
    print("yes")
else:
    print("no")
