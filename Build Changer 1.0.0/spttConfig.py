import os
def intro():
    os.system('cls')
    print('''
Before using the program for build installing, make sure that you have the needed build in your local repository.

In case there is no needed build, copy it using the program downloader and then use the build for further work.

- To begin to work with SPTT Version 9.1, enter 1

- To begin to work with SPTT Version 9.2, enter 2

- To open the local repository folder, enter "RF"
''')
    spttConfigVersion = input('Enter your answer here: ')
    return spttConfigVersion
