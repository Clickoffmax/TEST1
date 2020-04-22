import random

bullets = [0 for i in range(6)]
bullets[0] = 1
a = input(('введи 1 для того, чтобы играть и 0 для того, чтобы прекратить играть: '))

while a != '0':
    if random.choise(bullets) == 0:
        print('вы выиграли')
    else:
        print('вы проиграли')
    a = input(('хочешь сыграть еще \nВведи 1 для того, чтобы играть и 0 для того, чтобы прекратить играть: '))

