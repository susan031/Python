from colorama import init, Fore

init(autoreset = True)

spells = ["убить", "забить", "побить", "отменить", "набить"]

print(f"{Fore.GREEN}1 - Изучить новое заклинание\n2 - Показать книгу заклинаний\n3 - Тренироваться\n4 - Применить заклинание\n5 - Выход")

while True:
	userinput = input("\n>> ")

	if userinput == "1":
		spellinput = input("\nВведи заклинание: ")
		if spellinput.lower() not in spells:
			spells.append(spellinput)
			print(f"{Fore.GREEN}Добавлено")
		else:
			print("Заклинание есть")

	elif userinput == "2":
		for item in spells:
			print(item)

	elif userinput == "3":
		spellinput = input("\nВведи заклинание: ")
		if spellinput.lower() not in spells:
			print(f"{Fore.RED}Заклинание не изучено")
		else:
			for i in range(1, 4):
				print(f"{spellinput}")

	elif userinput == "4":
		spellinput = input("\nВведи заклинание: ")
		if spellinput.lower() not in spells:
			print(f"{Fore.RED}У вас не такого заклинания")
		else:
			print("Вы произнесли заклинание")

	elif userinput == "5":
		quit()

	else:
		print(f"{Fore.RED}Неверный ввод")