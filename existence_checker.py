import os

inp = input('Filename: ')

sa = str('D:\\' + inp + '')

print(sa)

check = os.access(sa, os.F_OK)

print(check)

if check == True:
    print('Папка существует')
    
else:
    print('Папки не существует')
