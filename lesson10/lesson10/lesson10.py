s = 'hello'
print (len(s)) #dlina stroki po simvolam
s2 =s.capitalize() #delaet 1i simvol s zaglavnoyi bykvi
print(s, s2) 
print (s.center(20, '!')) #otcentrirovanie gde est' probeli 1 chifra - probeli, 2 - sto vmesto probela
print (s. count('l', 0,4)) #chitaet simvoli 1 chifra - otkyda 2 - do kyda
print (s.find('a')) #pozicya v stroke
print (s.index('o')) 
print (s.replace('l', 't')) #zamenyaet bykvi
s = 'hello, world'
print (s.split(',')) #razbitie strok
print (s.isdigit()) #vipolnaytca ili net yslovie (cifri)
s = 'helloworld'
print (s.isalpha()) #a zdes iz bykv