# set - mnozestva s pomosiu {}

s={'apple','orange','apple','pear', 'orange', 'banana'}
s2= set ('hello')
s3 ={i for i in range(1,11)}
print(s)
print(s2)
print(s3)


s4 = {5, 3, 10, 1, 9, 2}
s4 = set() #�������� ������� ���������
print(s4)
print(s4)


nums = [1,2,3,3,1,2,4,5]
nums2 = set(nums)
print(nums2)

a = set ('abracadabra')
b = set('alacazam')
c = a - b #������� �� � ��� ����� ������� ���� � �
d = a | b #����������� ���� ��� � � ��� � �
e = a & b #����� � � � � �
f = a ^ b #����� � � ��� �, �� �� � �����
print(a,b,c,d,e,f, sep='\n')


s={'apple','orange','apple','pear', 'orange', 'banana'}
s2= s.copy() #���������� ����� ���������
print(s,id(s))
print(s2,id(s2))

s={'apple','orange','apple','pear', 'orange', 'banana'}
s.add('melon') #��������� ��-� �� ���������
print(s)

s={'apple','orange','apple','pear', 'orange', 'banana'}
s.remove ('apple') #������� ��-� �� ���������
if 'apple' in s:
     print('OK')
print(s)
#s.discard('apple2') #���� ��-�� ��� �� �� ������� ������



s={'apple','orange','apple','pear', 'orange', 'banana'}
s.clear() #�������
print(s)


a = frozenset ('hello') #������ ������ ������
print(a)