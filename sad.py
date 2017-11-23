import os
import shutil as sh

path = r'D:\Python Task'

path2 = os.path.join('C:')


def copycheck_file():
        
    files = os.listdir(path)

    files = [os.path.join(path, file) for file in files]
    
    files = [file for file in files if os.path.isdir(file)]

    filename = str(max(files, key=os.path.getctime))

    return filename

         
sa = str(path2)

check = os.access(sa, os.F_OK)

if check == False:
    
    sh.copytree(copycheck_file(), path2)

    newpath = path2 + '\\New Folder'

    newcheck = os.access(newpath, os.F_OK)

    print(newpath)
    
    if newcheck == True:
        
        print('Скопировалось')
    
else:
    
    sh.rmtree(path2)
    
os.system('pause')
