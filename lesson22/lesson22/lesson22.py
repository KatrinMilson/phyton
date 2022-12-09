# set - mnozestva s pomosiu {}

s={'apple','orange','apple','pear', 'orange', 'banana'}
s2= set ('hello')
s3 ={i for i in range(1,11)}
print(s)
print(s2)
print(s3)


s4 = {5, 3, 10, 1, 9, 2}
s4 = set() #создание пустого множества
print(s4)
print(s4)


nums = [1,2,3,3,1,2,4,5]
nums2 = set(nums)
print(nums2)

a = set ('abracadabra')
b = set('alacazam')
c = a - b #убирает из а все буквы которые есть в б
d = a | b #Обьединение букв или в а или в б
e = a & b #буквы и в и в б
f = a ^ b #буквы в а или б, но не в обоих
print(a,b,c,d,e,f, sep='\n')


s={'apple','orange','apple','pear', 'orange', 'banana'}
s2= s.copy() #возвращает копию множества
print(s,id(s))
print(s2,id(s2))

s={'apple','orange','apple','pear', 'orange', 'banana'}
s.add('melon') #добавляет эл-т во множество
print(s)

s={'apple','orange','apple','pear', 'orange', 'banana'}
s.remove ('apple') #удаляет эл-т из множества
if 'apple' in s:
     print('OK')
print(s)
#s.discard('apple2') #если эл-та нет то не выводит ошибку



s={'apple','orange','apple','pear', 'orange', 'banana'}
s.clear() #очистка
print(s)


a = frozenset ('hello') #ничего нельзя менять
print(a)