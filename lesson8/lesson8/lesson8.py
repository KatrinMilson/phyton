#stroki
# coding=windows-1251

words = 'Hello, word!' #obiyavlenie stroki
print (words)

words = 'Hello, "word"!' #obiyavlenie stroki
print (words)

words = "Hello, 'word'!" #obiyavlenie stroki
print (words)


words = "Hello, \"test\" 'word'!"  #ikraniryushui simvol
print (words)

words = "Hello, \ test 'word'!"  #ne ikraniryushui simvol
print (words)

words = "Hello, \test 'word'!"  #ikaniryushuya posledovatel'nost'
print (words)

words = "Hello, \\test 'word'!"  #ne ikraniryushui posledovatel'nost'
print (words)

verse = ('�� ���� - ������ ���� \n'
     '������� ��� ��� ����� ��� ������,')
print (verse)