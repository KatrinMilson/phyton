#zadacha 1

l = [1, 2, 3]
l2 = [i*2 for i in l]
print (' ')
print (l2)


#zadacha 2

l = [1, 2, 3]
sum = 0
for i in l:
    sum += i ** 2
print (sum)

#zadacha 3

time1 = 3
time2 = 6.7
time3 = 11.8 
a = time1//2
b = time2//2
c = time3//2
print (a, b, c)

#ili

litr = 0.5
t1 = 3
t2 = 6.7
t3 = 11.8
a = litr*t1
b = litr * t2
c = litr * t3
print (int(a)) and (int(b))
print (int(b))
print (int(c))

#zadacha 4

s = 'Hello world'
if ' ' in s:
    s = s.upper()
else:
    s = s.lower ()
print (s)