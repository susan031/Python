def has_unique_digits(n):
    return len(str(n)) == len(set(str(n)))

count = sum(has_unique_digits(i) for i in range(100, 10000))

print(f"Количество чисел с разными цифрами: {count}")
input("Press any key...")