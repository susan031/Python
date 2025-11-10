while True:
	text = input("Введи текст: ").strip()
	reserved_words_input = input("Введи список зарезервированных слов через запятую: ").strip().split(',')

	reserved_words = set([word.strip().lower() for word in reserved_words_input])

	words = text.split(' ')

	result_text = []
	for word in words:
	    cleaned_word = ''.join(e for e in word if e.isalnum())
	    if cleaned_word.lower() in reserved_words:
	        result_text.append(word.upper())
	    else:
	        result_text.append(word)

	output_text = ' '.join(result_text)
	print(output_text)