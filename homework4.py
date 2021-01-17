print("привет!")
number = int(input("Введите целое положительное число:"))
max = 0
num = number

while num > 0:
    past = num % 10
    if past > max:
        max = past
        break
    num = num // 10
print(f"Наибольшая цифра в числе {number} равна {max}")









