while True:
	usertext = input("Введи текст: ")
	bannedwords = input("Введи список матюков: ").lower().split(",")

	bannedwords = [word.strip() for word in bannedwords]

	words = usertext.split()

	for i in range(len(words)):
		if words[i].lower().strip(".,!?") in bannedwords:
			words[i] = "***"

	newtext = " ".join(words)
	print(newtext)