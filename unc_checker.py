import os

check = os.access('\\\\orpo-tfs-buildbot.elcom.local\Artifact share\Binaries (NOT ENCRYPTED, FAST BUILD)', os.F_OK)
print(check)
if check == True:
    print('Папка существует')
    
else:
    print('Папки не существует')
    
os.system('pause')
