print("Здравствуйте!")
data = input("Введите строку из нескольких слов разделенных пробелами:").split()

for n, i in enumerate(data, 1):
    print(n, i) if len(i) <= 10 else print(n, (i[:10]))

