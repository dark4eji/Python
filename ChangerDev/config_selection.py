import os


def config_selection(x, y):

    os.system('cls')

    print('''
---- Окно выбора ВЕРСИИ ''' + x + ''' ----

---- Выберите требуемое действие и введите ваш ответ ниже ----

- Чтобы установить билд SmartPTT Enterprise, введите "E".

- Чтобы установить билд SmartPTT PLUS, введите "P".

- Чтобы установить билд SmartPTT Developer, введите "D"

- Чтобы активировать "Загрузчик", введите "DD"

Введите ваш ответ: ''')

    get_config = (input('')).lower()

    if get_config in 'e':
        build_name = str('ent*')
        return build_name

    elif get_config in 'p':
        build_name = str('plus*')
        return build_name

    elif get_config in 'd':
        build_name = str('dev*')
        return build_name

    else:
        print(y)
        os.system('pause')
        os.system('cls')