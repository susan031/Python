try:
    input1 = int(input('Введи первое число диапазона: '))
    input2 = int(input('Введи второе число диапазона: '))

except ValueError:
    print("Некорректное число!")

for i in range(input1, input2):
    for j in range(1, 11):
        print(f"{i} x {j} = {i * j}")
    print()

input('')