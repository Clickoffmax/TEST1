
'hw 5 #3 удаление всех гласных'


text = input('введите тест: ')
len_txt = len(text)
print(len_txt)

translatedText = text.lower()


# def translate(text):
# for i in text:
#     if i == 'a':
#         i = ''
#     translatedText = translatedText + i
# print(translatedText)

translatedText = translatedText.replace('a', '')
translatedText = translatedText.replace('o', '')
translatedText = translatedText.replace('y', '')
translatedText = translatedText.replace('e', '')
translatedText = translatedText.replace('u', '')
translatedText = translatedText.replace('i', '')

print(translatedText)
