print("это программа для перевода секунд")

time = int(input("введите время в секундах:"))
min = 60

sec = time // min
print(time // min)
hour = sec // min
print(sec // min)
print(f"{hour}:{sec}:{time}")



