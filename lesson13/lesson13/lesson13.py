#while True:
#   print ('Hello') #бесконечный цикл


i = 1
while i <= 10:
    print(i, end=' ')
    i+= 1 #cokrashenie


print ('Hello', 'world', sep ='!', end = ' | ')
print ('Hello2', 'world2')

s = 'Hello, world'
for l in s:
    print(l, end =' ')


s = 'Hello, world'
for l in s:
     if l == ' ':
         continue #sleg operacia cikla
     print (f'"{l}"', end = ' ')


for i in 'Hello, world':
     if i == ' ':
         break #zavershit' cikl
     print(i, end =' ')
else: 
     print ('\n No spaces')


#Mini-homework

i=1900
while i<=2022:
     print(i, end= ' ')
     i+=1

    