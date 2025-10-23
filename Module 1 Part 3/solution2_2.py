number = input("Введите четырехзначное число: ")
digits = list(map(int, number))
digit1, digit2, digit3, digit4 = digits
product = digit1 * digit2 * digit3 * digit4
print(f"{digit1}*{digit2}*{digit3}*{digit4}={product}")
input("")