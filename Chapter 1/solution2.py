firstValue = input('Зарплата: ')
secondValue = input('Сумма месячного платежа: ')
thirdValue = input('Задолженность за комуналку: ')

firstValue = int(firstValue)
secondValue = int(secondValue)
thirdValue = int(thirdValue)

summ = firstValue-secondValue-thirdValue

print(f'Остаток денег: {summ}')

input("")