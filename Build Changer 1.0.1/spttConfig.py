import fnmatch
import os

wrong_answer = 'Некорректный ответ, попробуйте снова'

enter_answer = 'Введите ваш ответ здесь: '

path = os.listdir(r'D:\Python task')

config_path_list = []

finalchoice = []


def general_intro_func():

    def intro():
        # os.system('cls')
        print('''
Перед использованием программы следует убедиться, что требуемый билд находится в локальном репозитории.

Если билд отсутствует, скопируйте его используя встроенный загрузчик, а затем установите билд.

- Для начала работы с версией SmartPTT 9.2 введите 1

- Для начала работы с версией SmartPTT 9.3 введите 2

- Чтобы открыть локальный репозиторий, введите "RF"
''')
        sptt_config_version = input('{}'.format(enter_answer))
        return sptt_config_version

    def version_selecting(input_value):

        if input_value in ('1', '2'):
            input_value = int(input_value) + 1
            return str('9.' + str(input_value))

        elif input_value in ('RF', 'rf'):
            print(os.startfile('D:\Python develop'))
            os.system('cls')
            return general_intro_func()

        else:
            print(wrong_answer)
            os.system('pause')
            os.system('cls')
            return general_intro_func()

    return version_selecting(intro())


def config_selecting_screen(version_selecting_value):

    os.system('cls')

    print('''
---- Окно выбора ВЕРСИИ ''' + version_selecting_value + ''' ----

---- Выберите требуемое действие и введите ваш ответ ниже ----

- Чтобы установить билд SmartPTT Enterprise, введите "E".

- Чтобы установить билд SmartPTT PLUS, введите "P".

- Чтобы активировать "Загрузчик", введите "DD"
''')
    sptt_config_selecting = input('{}'.format(enter_answer))

    def config_selecting_processor(input_value):

        input_value = input_value.lower()

        if input_value in 'e':
            print('Вы выбрали Энтерпрайз')

        elif input_value in 'p':

            build_name = str('plus' + '*')
            print(type(build_name))
            return build_name

        else:
            print(wrong_answer)
            return(config_selecting_screen(sptt_config_selecting))


    config_selecting_processor(sptt_config_selecting)

config_defined = config_selecting_screen(general_intro_func())


def check_and_find(x):

    while True:
        try:
            for files in path:

                if fnmatch.fnmatch(files, x):

                    config_path = os.path.join('D:\\', 'Python task', files)
                    config_path_list.append(config_path)

            for dirs in config_path_list:

                last_edited_config = max(config_path_list, key=os.path.getctime)
                finalchoice.append(last_edited_config)

            check = os.access(finalchoice[0], os.F_OK)

            if check == True:
                print('Папка существует')
                print(finalchoice[0])
                break

            os.system('pause')

        except NameError:
            print('Нету файлов вообще епта')
            config_selecting_screen(general_intro_func())

check_and_find(config_defined)



