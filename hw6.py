file_path = 'txtstat.txt'
file_path2 = 'outputstat.txt'

file = open(file_path)
file_output = open(file_path2, 'w')

content = file.readlines()
print(content)
summa = 0
srez = 0

for line in content:
    print(line)
    "беру одну линию"
    srez = line[0:-1]
    "отрезаю перенос строки"
    print(srez)
    "проверяю срез распечатываенем"
    for i in srez:
        summa += int(i)
        "суммирую цифры в срезе"
    print(summa)
    "печатю сумму среза"
    print(summa/len(srez))
    "печатю печатю печатю среднее среза"
    file_output.write(str(summa) + '\n')
    "записываю в новый файл сумму среза"
    file_output.write(str(summa/len(srez)) + '\n')
    "записываю в новый файл среднее среза"








file.close()