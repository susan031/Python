from colorama import init, Fore

init(autoreset=True)

while True:
    try:
        xvalue = int(input("Введи значение x: "))
        yvalue = int(input("Введи значение y: "))
    except ValueError:
        print(f"{Fore.RED}Введено неверное значение!\n")
        continue

    print(f"{xvalue**yvalue}\n")