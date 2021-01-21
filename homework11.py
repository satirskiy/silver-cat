print("hi")
my_list = [10, 9, 8, 7, 3, 3]
new_number = int(input("введите число:"))
i = 0
for n in my_list:
    if new_number <= n:
        i += 1
my_list.insert(i, new_number)
print(my_list)
