count = 0

for number in range(100, 1000):
    s = str(number)

    unique_digits_count = len(set(s))

    if unique_digits_count == 2 or 3:
        count += 1

print("Количество чисел с двумя одинаковыми цифрами:", count)
input("Press any key...")