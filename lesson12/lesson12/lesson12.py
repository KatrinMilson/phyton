# coding=windows-1251

if 1:
     print ('���������� �������')
else:
    print('��������� �����')


light = 'blue'
if light == 'red':
     print ('Stop')
elif light == 'yellow':
     print (' Wait')
elif light == 'green':
     print('Go')
else:
     print('What?')


age = int(input('������� ��� ���? ')) #������ ������������
if age >= 18:
    print('����� ����������!')
else:
    print ('��� ��� ����')

age = int(input('������� ��� ���? ')) #������ ������������
if age >= 18:
    print('����� ����������!')
else:
    print (f'��� {age} ���, �� ������� {18 - age} ')


time = 11
if time < 12 or time > 13: #dva yslovia
    print ('Open')
else:
        print ('Close')

   
        
time = 11
day = 'st'
if time >= 8 and day != 'su': 
    print ('Open')
else:
        print ('Close')

x = 0
if not x:
    print('OK')
else: 
    print('NO')


x = 1
res = 'OK' if x else 'NO'
print(res)
print ('OK' if x else 'NO')