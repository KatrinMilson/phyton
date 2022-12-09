# coding=windows-1251
#import os
#import random
#print(os.getcwd())

#print (random.randint(1, 100))


# print(randint(1,100))
# l = [1,2,3,4,5,]
# shuffle(l)
# print(l)

# import os
# import os  as my 

# print(os.getcwd())
# print(my.getcwd())
 
# import libs

# print(libs.get_count('hello', 'l'))
# print(libs.get_len('hello'))


# f= libs.get_count
# print(f('hello', 'l'))

# def get_sum (a,b):
#     return a+b

# func = get_sum
# print(func(1,2))

#dz 
import random


n="нет"
y="да"
while n != y:
    from random import randint 
    a = int(randint(1,101))
    b = int(input('Введите угадываемое число от 1 до 100: '))
    c = 0
    while b != a:
        if b>a:
            print(f'Угадываемое число меньше чем {b}')
        elif  b<a:
            print(f'Угадываемое число больше чем {b}')
        b = int(input('Введите угадываемое число от 1 до 100: '))
        c += 1
    print(f'Вы угадали число {a} за {c} попыток!')
    y = input('Начать заново?\n(yes or no): ')
    print()
    print()