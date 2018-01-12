import os

guideloc = "D:\Repositories\docs_ascii\Dispatcher Quick User Guide\EN\Dispatcher Quick User Guide.adoc"
topicspath = r"D:\Repositories\docs_ascii\Dispatcher Quick User Guide\EN\topics\\"
session = None # Объявление переменных для обработчика префиксов
pref = None    #

while True: # Обработчик префиксов

    getpref = input("Что создаём: инструкцию или описание?[INS/UI]: ")

    if getpref in "INS":
        pref = getpref + "_"
        session = "инструкционных "
        break

    elif getpref in "UI":
        pref = getpref + "_"
        session = "описательных "
        break

    else:
        print("Неверное значение, еще раз")

while True:

    os.system('cls')

    print("Cеанс создания " + session + "топиков\n"
          "Введите stope, чтобы прервать программу: ")

    filename = input("Имя топика: " )

    if filename not in "stope":

        name = pref + filename.replace(" ", "_") + ".adoc"
        include ="\n//" + filename + "\n:leveloffset: 0\ninclude::{t}\\" + name + "[]"
        pathtop = topicspath + name

        with open(pathtop, 'a') as f:
             f.write("== " + filename)

        with open(guideloc, 'a') as g:
             g.write(include)

    else:
        break

os.system('pause')
