# def greet():
#     print('hello')
#
#
# def print_imp(text):
#     print(text.title())
#
#
# def summa(a,b):
#     print(a+b)
#
# summa(b='world',a='Hello ')



# a = input()
# print_imp(a)


# def summa(a='привет, ',b='мир'):
#     print(a+b)
#
#
# summa()

def summa(a='привет, ',b='мир'):
    return a + b


# a = input()
# print(len(a))
# print(summa())


import random


def get_name():
    name = input("Введите ваше имя: ")
    return name.strip().title()


def generate_number(name_length):
    name_length = len(name_length)
    rand_str = ''
    for i in range(name_length):
        rand_num = random.randint(1, name_length)
        rand_str += str(rand_num)
    return rand_str


# def get_full_data():
#     name = get_name()
#     number = generate_number(name)
#     return name + ' ' + str(number)
#
#
# print(get_full_data())

#
# def get_full_info(name, surname, otchestvo):
#     """Возвращает аккуратно отформатированное полное имя."""
#     if otchestvo:
#         full_name = name.strip().title() + ' ' + otchestvo.strip().title() + ' ' + surname.strip().title()
#     else:
#         full_name = name.strip().title() + ' ' + surname.strip().title()
#     return full_name
#
#
# name_of_user = input("Введите ваше имя: ")
# othestvo = input("Введите ваше отчество: ")
# surname_of_user = input("Введите вашу фамилию: ")
#
#
# print(get_full_info(name_of_user, surname_of_user, othestvo))


#
# person = {'names':[], 'surnames': []}
#
#
# def create_person(name, surname):
#     """Возвращает словарь с информацией о человеке"""
#     person['names'].append(name)
#     person['surnames'].append(surname)
#     return person
#
#
# user_size = int(input("Введите количество пользователей, которые должны появиться в  этом словаре: "))
# for user in range(user_size):
#     name = input("Введите имя пользователя")
#     surname = input("Введите фамилию пользователя")
#     create_person(name, surname)
#
# print(person.items())


a = [1,2,3]

def four(spisok):
    duplicate = spisok[:]
    duplicate.append(4)
    return duplicate

print(a)
print(four(a))
print(a)