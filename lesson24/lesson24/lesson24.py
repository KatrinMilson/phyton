prod = {'title': 'Sony', 'Price': 100}
print(prod.items())
print(prod.keys())
print(prod.pop('title', 'NO'))
print(prod)
print(prod.popitem())
print(prod)
print(prod.setdefault('title2','test'))
prod.update({'test': 'value'})
prod.update({'Price': 200})
print(prod)
print(prod.values())

# dict.clear() - ������� �������
# dict.copy() - ���������� ����� �������
# dict.get(key[, default]) - ���������� �������� �����, �� ���� ��� ���, �� ������� ����������, � ���������� default (�� ��������� None)
# dict.items() - ���������� ���� (����, ��������)
# dict.keys() - ���������� ����� � �������
# dict.pop(key[, default]) - ������� ���� � ���������� ��������. ���� ����� ���, ���������� default (�� ��������� ������� ����������)
# dict.popitem() - ������� � ���������� ���� (����, ��������). ���� ������� ����, ������� ���������� KeyError. �������, ��� ������� �������������
# dict.setdefault(key[, default]) - ���������� �������� �����, �� ���� ��� ���, �� ������� ����������, � ������� ���� � ��������� default (�� ��������� None)
# dict.update([other]) - ��������� �������, �������� ���� (����, ��������) �� other. ������������ ����� ����������������. ���������� None (�� ����� �������!)
# dict.values() - ���������� �������� � �������
