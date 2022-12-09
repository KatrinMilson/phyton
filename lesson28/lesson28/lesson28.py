# def get_sum(a,b):
#     """
#     :param a: shit1
#     :type a: int
#     :param b: shit2
#     :type b: int
#     """
#     return a+b
# print(get_sum(1,2))

a = 5 #global
def f():
    a = 10 #local
    a += 1
    print(a)
print (a)
f ()
print (a)


def f():
    global a
    a += 1
print (a)
f()
print (a)

l = [1, 2, 3]
def f(l):
    return [i * 2 for i in l]
print (f(l))

l = [1, '2', 3]
def f(l):
    return [i * 2 for i in l]
print (f(l))

l = [1, 2, 3]
def f2(l):
    def get_mult(x):
        return x*2
    return [get_mult(i) for i in l]
print (f2(l))

l = [1, 2, 3]
def f3(l):
    def get_mult(x):
        if isinstance(x, int):
            return x*2
        return [get_mult(i) for i in l if get_mult(i)]
    print (f3(l))

l = [1, 2, 3]
def f4(l):
    def get_mult(x):
            return x*2
    return list(map(get_mult, l))
    print (f4(l))


 #dz1

def odd_ball(arr):
    return arr.index ('odd') in arr
print (odd_ball(["even", 4, "even", 7, "even", 55, "even", 6, "even", 10, "odd", 3, "even"]))
print (odd_ball(["even",4,"even",7,"even",55,"even",6,"even",9,"odd",3,"even"]))
print (odd_ball(["even",10,"odd",2,"even"]))

#dz2


def find_sum(n):
    sum1 = 0
    for i in range(n+1):
        if i % 3 == 0 or i % 5 == 0:
            sum1 += i
    return sum1
print (find_sum(5))  
print (find_sum(10))  

#dz3

names = ["Ryan", "Kieran", "Mark", "John", "David", "Paul"]
def get_names(names):
    return [i for i in names if len(i) == 4]
print(get_names(names))
