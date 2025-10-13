numbers = []

while True:
    try:
        num = float(input("Введите число: "))
        numbers.append(num)
        
        if num == 7:
            break
            
    except ValueError:
        print("Ошибка! Введите действительное число.")

if len(numbers) > 0 and numbers[-1] != 7:
    total_sum = sum(numbers[:-1])
    max_value = max(numbers[:-1])
    min_value = min(numbers[:-1])
else:
    total_sum = sum(numbers)
    max_value = max(numbers)
    min_value = min(numbers)

print(f"Сумма введённых чисел: {total_sum}")
print(f"Максимальное число: {max_value}")
print(f"Минимальное число: {min_value}")

print("Good bye!")

input("")