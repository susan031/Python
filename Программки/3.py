import string

text = input("Введите текст: ")

sentences = text.replace('!', '.').replace('?', '.').count('.')

words = text.split()
num_words = len(words)

punctuations = string.punctuation
num_punctuations = sum(char in punctuations for char in text)

print(f'Предложений: {sentences}')
print(f'Слов: {num_words}')
print(f'Знаков препинания: {num_punctuations}')

input("")