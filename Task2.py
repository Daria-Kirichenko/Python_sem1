# Задача 2: Найдите сумму цифр трехзначного числа.

a = int(input("Введите трехзначное число: "))
print(a)
sum = 0
if a > 99 and a < 1000:
    while a != 0:
        lastDigit = a % 10
        sum = sum + lastDigit
        a = a // 10
    print(sum)
else:
    print("Ошибка: число должно быть трехзначным")
