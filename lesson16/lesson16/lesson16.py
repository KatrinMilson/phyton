name = ['Ivanov', 'Petrov', 'Sidorov']
print (name[2])

l  = [1, 2, 3, 'hello', ['test', 10], 'world', True]
print (l[4] [0])
print (l[0:3]) #srez
print (l)
l[2] = 'world' #zamena
print (l)
l[:2] = [10, 15] #izmenenie
print (l)

l.append ('new') #dobavlenie
print(l)

l.extend([5, 7]) #dobavlenie
print (l)

l2 = ['hi', 19] #slozenie
l += l2
print (l)

l.insert (1, 'test') #vstavlyaet x na kakyi-to poziciy so sdvigom
print (l)

l.remove ('world') #1-i element naidenni v spiske
print (l)

el = l.pop () #ydolyaet 1-i el-t i vozvrashaet ego
print (l, el)


el = l.pop (1) #ydolyaet 1-i el-t i vozvrashaet ego
print (l, el)

print (l, l.count ('test')) #chitaet kol-vo slov kakie nyzni

# l.sort () #tolko dlya odnotipnix znacheniy 

l3 = ['hello', 'hi', 'David', 'world', 'test']
print (l, l.count('test'), l3, sep = '\n')
print ('h' > 'a')

l3 = sorted(l3) #sortiryet
print (l3)

#l.revers - razvorachivaet
#l.copy - kopiryet
#l.clear - ochihaet


