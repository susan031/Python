start = int(input("Введите начальное число диапазона: "))
end = int(input("Введите конечное число диапазона: "))

even_numbers = []  
odd_numbers = []  
multiples_of_9 = [] 

for i in range(start, end + 1):
    if i % 2 == 0:
        even_numbers.append(i)
    else:
        odd_numbers.append(i)
    if i % 9 == 0:
        multiples_of_9.append(i)

sum_even = sum(even_numbers)
sum_odd = sum(odd_numbers)
sum_multiples_of_9 = sum(multiples_of_9)

count_even = len(even_numbers)
count_odd = len(odd_numbers)
count_multiples_of_9 = len(multiples_of_9)

avg_even = sum_even / count_even if count_even > 0 else 0
avg_odd = sum_odd / count_odd if count_odd > 0 else 0
avg_multiples_of_9 = sum_multiples_of_9 / count_multiples_of_9 if count_multiples_of_9 > 0 else 0

print(f"Сумма чётных чисел: {sum_even}, Среднее: {avg_even:.2f}")
print(f"Сумма нечётных чисел: {sum_odd}, Среднее: {avg_odd:.2f}")
print(f"Сумма чисел, кратных 9: {sum_multiples_of_9}, Среднее: {avg_multiples_of_9:.2f}")
input("")