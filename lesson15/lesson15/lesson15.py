#coding=windows-1251

print ('Таблица умножения')
for i in range(1, 11):
    for j in range(1, 11):
        print(f'{i} * {j} = {i*j}\t', end=' ')
    print(' ')
