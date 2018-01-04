import fnmatch
import os

path = os.listdir(os.path.join('C:\\', 'ProgramData', 'Git'))

config_path_list = []

finalchoice = []


def folder_finder(x):

    for files in path:
        config_path = fnmatch.filter(path, x)

    for match in config_path:
        feel = os.path.join('C:\\', 'ProgramData', 'Git', match)
        config_path_list.append(feel)

    while True:

        try:
            for dirs in config_path_list:
                last_edited_config = max(config_path_list, key=os.path.getctime)
                finalchoice.append(last_edited_config)
                check = os.access(finalchoice[0], os.F_OK)

            if check is True:
                print('Папка существует')
                break


        except NameError:
            print('Нету файлов вообще епта')
            os.system('pause')
            break