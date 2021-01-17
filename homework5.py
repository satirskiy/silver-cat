revenue = int(input("Введите сумму выручки:"))#выручка
costs = int(input("Введите сумму издержек:"))#издержки
profit = revenue - costs #прибыль
if profit < costs:
    print("Убыток")
elif profit > costs:
        print("Прибыль")
if profit > costs:
    profitabbility = profit / revenue * 100 #рентабельность
    print(f"рентабельность{profitabbility }")
staff = int(input("Введите численость сотрудников:"))
print(f"прибыль на одного сотрудника {profit // staff}")
