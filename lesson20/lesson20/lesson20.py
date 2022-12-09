# coding=windows-1251

# #кортеж это не изменяемый список

#t1 = (1, 2, 3)
#print(type(t1))

#t2 = (1, 2, 3)

#t3 = tuple ((1, 2, 3))
#print (t3)

#t4 = (1,)
#print (t4)



#t5 = tuple ('hello') 
#print (t5)

#t1 = (1, 2, 3)
#print (t1.__sizeof__())

t1 = tuple ('hello')
t2 = tuple (' world')
t3 = t1 + t2
print(t3)
print (t3.count('l'))
if 'l' in t3:
    print(t3.index('l'))
else:
    print ('NO')

for i in t3:
    if i == ' ':
        continue
    print (f'"{i}"', end = ' ')

t1 = (10, 11, [1, 2, 3], [4, 5, 6], ['hello', 'world'])
print (t1, id (t1))
t1 [4][0] = 'new'
t1 [4].append ('hello')
print (t1, id (t1))

t1 = (1, 2, 3,)
x, y, z = t1
print (x, y, z)

x = 1
y = 2
print (x, y)
x, y = y, x
print (x, y)

#zd 1

words = ['мадам', 'топот', 'test', 'madam', 'word']
words1 = []
for i in words:
     #stroka perevopachivaetca
    if i == i[::-1]:
        words1.append(i)
print(words1)


#zd 2

my_str = ['Око за око', 'А роза упала на лапу азора', 'Около Миши молоко']
my_str1=[]
for i in my_str:
   k = (i.lower().replace(' ', ''))[::-1]
if k == k [::-1]:
        my_str1.append(i)
print(my_str1)
