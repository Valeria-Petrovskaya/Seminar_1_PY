number = int(input("Введите трехзначное число: "))
a = number // 100     # Первая цифра числа
b = (number // 10) % 10    # Вторая цифра 
c = number % 10    # Третья цифра
print(a+b+c)