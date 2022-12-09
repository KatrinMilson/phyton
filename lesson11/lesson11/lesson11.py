name = 'John'
age = 30
print ('My name is ' + name + '. I\'m ' + str(age)) #obedinenie stroki
print ('My name is %(name)s. I\'m %(age)d' %{'name': name, 'age': age}) #% kak marker stoby ne razrivat stroki
print ('My name is %s. I\'m %d' %(name, age)) #pozicionnie markeri po posledovatelnosti
print ('Title: %s, price: %.2f' %('Sony', 40)) #drobnaya chacti cherez float
print ('My name is {}. I\'m {}'.format (name, age)) 
print ('My name is {name}. I\'m {age}'.format (name=name, age=age))
print (f'My name is {name}. I\'m {age}') #f - formatirovannaya stroka
print (f'My name is {name}. I\'m {age + 5}') #f - formatirovannaya stroka
print ('5 + 2 = {}'.format(5+2))
print (f'5+2={5+2}')