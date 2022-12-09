#siraya stroka

#s = r'C:\d\new.txt' #r - siraya stroka
#print(s)

#s = 'Py' 'thon'
#print(s)

s1 = 'Hello, '
s2 = 'world!'
s3 = s1 + s2
print (s3)

name = 'John'
age = 20

print('My name is ' + name + " I'm " + str(age))
print(' hi  ' * 5) #dyblirovanie stroki

#s = 'Hello world!'
#print(s[0]) #index iz posledovatelnosti
#print(s[-12]) #kol-vo simvolov dlya index mozet byit + i -
#s[0] = 'D' #ne mozem perepisat 0 simvol


#[X:Y:Z] #x - hachalo y- okonchanie z - kol-vo creza

s = 'Hello world!'
print (s[0:12]) #vivodit Hello world!
print(s[-1]) #vivodit !
print(s[0:5]) #vivodit Hello
print(s[:5]) #vivodit Hello
print(s[6:]) #vivodit world!
print(s[::2]) #vivodit Hlowrd opeskaet kazdiu vtoroy simvol
print(s[::-1]) #vivodit !dlrow olleH
print(s[:5 ] + s[6:]) #vivodit Helloworld!


