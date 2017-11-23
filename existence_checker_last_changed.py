import fnmatch
import os

path = os.listdir(r'D:\Python task')

config_path_list = []

finalchoice = []

print(finalchoice)

def check_and_find(ler):



    while True:
        try:
            for files in path:

                if fnmatch.fnmatch(files, ler):

                    config_path = os.path.join('D:\\', 'Python task', files)
                    config_path_list.append(config_path)

            for dirs in config_path_list:

                last_edited_config = max(config_path_list, key=os.path.getctime)

                finalchoice.append(last_edited_config)

            check = os.access(finalchoice[0], os.F_OK)

            if check is True:

                print('Папка существует')
                print(finalchoice[0])
                break

            os.system('pause')

        except NameError:
            print('Нету файлов вообще епта')
            break

check_and_find('plus*')