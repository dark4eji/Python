import random as l
import os

rannumb = l.randint(1, 100)

basenumber = 10

def greets():
    print('''Добро пожаловать в игру "Угадай число"

Ваша задача угадать число от 1 до 100.

Вам дается 10 попыток.
''')
greets()

trycollector = []

check = True

while check == True:

    while True:
        try:
            number = int(input('\nВведите сюда ваше число: '.upper()))

            if type(number) == int:
                break
        except ValueError:
            number = None
            print('Введите число, пожалуйста!')



    trynumb = 0

    trynumb += 1

    basenumber -= 1

    if trynumb == 10 or basenumber == 0:
        print('\nУ вас закончились попытки, перезапустите, пожалуйста, программу')
        break


    if number > rannumb:

        if trynumb > 0:
            os.system('cls')
            trycollector.append(number)
            print('Использованные вам числа: {}'.format(trycollector))

        print('\nЧисло {} больше загаданного!\n'.format(number) +
              '\nОсталось {} попыток'.format(basenumber))

    elif number < rannumb:

        if trynumb > 0:
            os.system('cls')
            trycollector.append(number)
            print('Использованные вам числа: {}'.format(trycollector))

        print('\nЧисло {} меньше загаданного!.\n'.format(number) +
              '\nОсталось {} попыток'.format(basenumber))


    elif number == rannumb:
        print('\nПоздравляем, вы угадали число!! Это {}\n'.format(rannumb))

        while True:

            mlek = input('\nХотите еще один заход? (да, нет): ')

            if mlek == "да":
                basenumber = 10
                trynumb = 0
                print('У вас 10 попыток')
                break

            elif mlek == "нет":
                print('\nДо свидания!')
                check = False
                os.system('pause')
                break

            if mlek != 'да':
                print('\nВведите "да" или "нет"')

            elif mlek != 'нет':
                print('\nВведите "да" или "нет"')
