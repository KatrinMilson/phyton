# coding=windows-1251

x = 75
user_num = 0
cnt = 0

while True:
    user_num = int(input('� ������� ����� �� 1 �� 100 - ������ ���: '))
    cnt += 1
    if user_num == x:
        print(f'�� ������ ����� �� {cnt} �������')
        print('������� �� ����')
        break
    elif user_num > x:
        print('��� ����� ������')
    else:
        print('��� ����� ������')