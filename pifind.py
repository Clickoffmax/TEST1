file_path = 'pifile.txt'
file = open(file_path)
data = input('введите дату своего рождения в формате ДДММ')
content = file.read()
index = content.find(data)
if index != -1:
    print('дата вашего рождения есть в числе Пи на месте', index - 1)
else:
    print('даты вашего рождения нет в числе Пи')


file.close()