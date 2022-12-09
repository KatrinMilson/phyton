d = {}
prod = {'title': 'Sony', 'price': 100}
prod2 = dict(title = 'iphone', price=110)

print(d)
print(prod)
print(prod2)
print(type(d))

users = [
     ['bob@gmail.com', 'Bob'],
     ['katy@gmail.com', 'Katy'],
     ['john@gmail.com', 'Jonh']
]
d_users=dict(users)
print(users)
print(d_users)



users_t= (
     ('bob@gmail.com', 'Bob'),
     ('katy@gmail.com', 'Katy'),
     ('john@gmail.com', 'Jonh')
)
t_users=dict(users_t)
print(users_t)
print(t_users)


prod3 =dict.fromkeys(['price1','price2','price3' ], 50)
print(prod3)

nums = {i: i + 1 for i in range (1,10)}
print (nums)


prod3 = {'title': 'Sony', 'Price': 100}
prod4 = dict(title = 'Iphone', price=110)
print( prod3['title'])
print( prod3.get('title2', 'NO')) #if no kay

for key in prod3:
    print(f'{key}: {prod3[key]}')
print(prod3[key])

for key, value in prod3.items():
    print(key, value)


prods= [
     {'title': 'Sony', 'Price': 100},
     {'title': 'iPhone', 'Price': 110},
     {'title': 'Samsumg', 'Price': 90}
 ]
print(prods)

for prods in prods:
     print(prods['title'], prods['Price'])
