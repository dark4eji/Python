import os


def version_selection(x):

    os.system('cls')

    print('''
Перед использованием программы следует убедиться, что требуемый билд находится в локальном репозитории.

Если билд отсутствует, скопируйте его используя встроенный загрузчик, а затем установите билд.

- Для начала работы с версией SmartPTT 9.2 введите 1    

- Для начала работы с версией SmartPTT 9.3 введите 2

- Чтобы открыть локальный репозиторий, введите "RF"
    
Введите ваш ответ:''')

    get_version = input('')

    if get_version in ('1', '2'):
        version_choice = int(get_version) + 1
        return '9.' + str(version_choice)

    elif get_version in ('RF', 'rf'):
        print(os.startfile('D:\Git'))
        os.system('cls')

    else:
        print('Weong')
        os.system('pause')
        os.system('cls')