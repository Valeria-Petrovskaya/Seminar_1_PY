n = int(input("Введите количество долек n: "))
m = int(input("Введите количество долек m: "))
k = int(input("Введите количество отломленных долек: "))
if k <= n * m and (k % n == 0 or k % m == 0):
    print("Yes")
else:
    print("No")
