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

verse = ('Всё тихо - полная луна \n'
     'Блестит как меж ветел над прудом,')
print (verse)