# def hello():
#         return 'Hello, i am func "hello" '
#
#
# def super_func(func):
#     print('Hello, i am func "super_func" ')
#     print((func()))
#
# super_func(hello)
#
#
# def hello():
#     return 'Hello, i am func "hello" '
#
# test = hello
# print(test())

# def my_decorator(func):
#     def func_wrapper():
#         print('Code before')
#         func()
#         print('Code after')
#
#     return func_wrapper
#
#
# @my_decorator
# def func_test():
#     print('Hello, i am func "func_test"')
#
#
# test = my_decorator(func_test)
# test()


def make_title(fn):
    def wrapped():
        title = fn()
        title = title.capitalize()
        title = title.replace(',', '')
        return title

    return wrapped


@make_title
def hi():
    return 'hello, world'


print(hi())
