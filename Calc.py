while True:
     
     print('''Классический калькулятор:

- Использовать - для вычитания

- Использовать + для сложения

- Использовать * для умножения

- Использовать / для деления

- Использовать ^ для возведения в степень
''')
     
     def calc():
        error = 'Operation please'       
        test = input('Введите сюда требуемую операцию: ')
        lst = list(test)
        op = ['+', '-', '*', '/', '^']

        def get_numbers():

            if '+' in lst:
                sign = lst.index('+')
                ass = a + b

            elif '*' in lst:
                sign = lst.index('*')


            elif '/' in lst:
                sign = lst.index('/')


            elif '-' in lst:
                sign = lst.index('-')


            elif '^' in lst:
                sign = lst.index('^')


            else:
                print(error)
                del sign
                calc()


        def body(x):
             ass = None
             firstPart = lst[:x]
             secondPart = lst[x:]
             secondPartNoSign = secondPart[1:]
             
             while True:
                 try:
                    a = float(''.join(firstPart))
                    b = float(''.join(secondPartNoSign))
                    print(ass)
                    if lst[x] not in op:
                        print('Wrong operation')
                        break
                
                 except (ValueError, UnboundLocalError):
                      print('Only numbers are operable')
                 calc()
     


        get_numbers()
        print(sign)
        body(sign)

                       
        
     calc()
        
     
        
   




