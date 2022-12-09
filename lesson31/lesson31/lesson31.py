# coding=windows-1251

from datetime import date, datetime, timedelta
import locale

# class date

today = date.today()
print(today) #2022-12-07
print(today.day) #7
print(today.month) #12
print(today.year) #2022
print(today.weekday()) #2

# class datetime
now = datetime.now() 
now2 = datetime.today()
print(now, now2, sep= ' ')  #2022-12-07 15:54:42.742799
print(now.day) #7
print(now.month) #12
print(now.year) #2022
print(now.weekday()) #3
print(now.hour) #15
print(now.minute) #54
print(now.second) #42

days = ['пн', 'вт', 'ср', 'чт', 'пт', 'сб', 'вс']
print(days[now.weekday()]) #cp

now = datetime.now()
locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8') #na pysskom
print(now) 
print(now.strftime('%a')) #cp
print(now.strftime('%A')) #среда
print(f'Дата: {now.strftime("%A, %d %b %Y")}') #Дата: среда, 07 дек 2022
print(f'Время: {now.strftime("%H:%M:%S")}') #Время: 16:04:19

print(now.strftime('%c')) #07.12.2022 16:04:19
print(now.strftime('%x')) #07.12.2022
print(now.strftime('%X')) #16:04:19

now = datetime.today()
print(now.strftime('%c')) #07.12.2022 16:04:19
d1 = now + timedelta(days=1, hours=2, minutes=10)
print(d1.strftime('%c')) # 08.12.2022 18:14:19