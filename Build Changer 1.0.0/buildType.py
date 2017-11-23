import os
def buildTypeLetter(x):
        os.system('cls')
        print('''
---- VERSION ''' + str(x) + ''' Action Selection Window ----

---- Choose the needed action and enter your answer below ----

- To install SmartPTT Enterprise build, enter "E".

- To install SmartPTT PLUS build, enter "P".

- To activate Downloader, enter "DD"
	''')
        buildTypeChoice = input('Enter your answer here: ')
        return buildTypeChoice
        
