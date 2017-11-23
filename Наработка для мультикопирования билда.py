import os
name = input('Enter build name: ')

a = list(name)

space = a.index(' ')

firstPart = a[:space]
secondPart = a[space:]
secondPartNoSign = secondPart[1:]
a = ''.join(firstPart)
b = ''.join(secondPartNoSign)
print(a)
print(b)

'''
if ' ' in Lst[0]:
    print('a')
else:
    print(Lst)
'''
