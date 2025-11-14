text = input("Введите текст: ")

words = text.split()

total_chars = len(text)

vowels = 'аеуёияоюэюы'
consonants = 'бвгджзйклмнпрстфхцчшщ'

num_words = len(words)
num_vowels = sum(char in vowels for char in text.lower())
num_consonants = sum(char in consonants for char in text.lower())

longest_word = max(words, key=len)

print(f'Количество слов: {num_words}')
print(f'Общее количество символов: {total_chars}')
print(f'Гласных букв: {num_vowels}')
print(f'Согласных букв: {num_consonants}')
print(f'Самое длинное слово: {longest_word}')

input("")