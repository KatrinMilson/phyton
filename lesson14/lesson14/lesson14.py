# coding=windows-1251

l = [1,2,3,'hello', ['test', 10], 'world', True] #[] dlya spiska
print(type(l))
print(l)
l2 = list('Hello')
print (l, l2, sep= '\n')
l3 = list ((1,2,3))
print (l, l2, l3, sep= '\n')

l4 = [i for i in 'hello'] #generator spiska

l5 =[i for i in 'hello world' if i != ' ' and i != 'e']
print(l, l2, l3,l4, l5, sep='\n')

l6 =[i for i in 'hello world' if i not in ['a', 'e', 'i', 'o', 'u', ' ']]
print(l, l2, l3,l4, l5, l6, sep='\n')

#range

print (list(range (10)))
print (list(range (1, 10)))
print (list(range (1, 11)))
l7 = list(range(0,11))
print (l7)

for i in range (1, 3):
    print (f'Внешний цикл #{i}')
    for j in range (1, 3):
        print (f'\tВнутренний цикл #{j}')

#homework

print('Таблица умножения')
for i in range(1, 11):
    for j in range(1, 11):
        print(f'{i} * {j} = {i * j}\t', end=' ')
    print(' ')
else:
    print('Done')
