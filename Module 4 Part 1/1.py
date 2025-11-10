while True:
	userinput = input(">> ")
	userinput = userinput.replace(" ", "")
	text = userinput[::-1]

	if userinput.lower() == text.lower():
		print("Палиндром есть")
	else:
		print("Палиндрома не")