import random

b = [1,2,3]
random.shuffle(b)


dictionary = {}

while True:
    key = input('введите слово на английском или stop, чтобы прекратить: ').lower().strip()
    if key == 'stop':
        break
    value = input('введите перевод или stop, чтобы прекратить: ').lower().strip()
    if value == 'stop':
        break
    dictionary[key] = value

dictionary = list(dictionary.items())

random.shuffle(dictionary)
dictionary = dict(dictionary)
print(dictionary)

print('Сейчас Вам будет предложено ввести данные в словарь и далее поиграть в угадалку ')
score = 0
errors = 0

for key, value in dictionary.items():
    word = input('введите перевод слова '+key+': ').lower().strip()
    if word == value:
        score += 1
    else:
        errors += 1
    if errors == 3:
        print('вы сделали 3 ошибки, игра закончена ')
        break
print(score)
print(errors)

"""
подсчет ошибок +
дружелюбие +
Перемешать элементы словаря 
Проигрыш при условии 3 ошиок +
переводить все вводные строки к нижнему регистру +
Удалить пробелы в вводных строках +

"""

