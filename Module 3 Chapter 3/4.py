while True:
    try:
        num = int(input("Введите целое число: "))
        break
    except ValueError:
        print("Некорректное число\n")

cleaned_num_str = str(num).replace('3', '').replace('6', '')

if cleaned_num_str == '':
    print("Результат пустой")
else:
    result = int(cleaned_num_str)
    print(result)
input('')