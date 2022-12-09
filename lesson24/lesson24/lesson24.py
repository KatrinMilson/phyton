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

# dict.clear() - очищает словарь
# dict.copy() - возвращает копию словаря
# dict.get(key[, default]) - возвращает значение ключа, но если его нет, не бросает исключение, а возвращает default (по умолчанию None)
# dict.items() - возвращает пары (ключ, значение)
# dict.keys() - возвращает ключи в словаре
# dict.pop(key[, default]) - удаляет ключ и возвращает значение. Если ключа нет, возвращает default (по умолчанию бросает исключение)
# dict.popitem() - удаляет и возвращает пару (ключ, значение). Если словарь пуст, бросает исключение KeyError. Помните, что словари неупорядочены
# dict.setdefault(key[, default]) - возвращает значение ключа, но если его нет, не бросает исключение, а создает ключ с значением default (по умолчанию None)
# dict.update([other]) - обновляет словарь, добавляя пары (ключ, значение) из other. Существующие ключи перезаписываются. Возвращает None (не новый словарь!)
# dict.values() - возвращает значения в словаре
