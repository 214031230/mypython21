#!/usr/bin/env python3
# import time
# count = 1
# while True:
#     with open("tmp", mode="a") as f1:
#         f1.write("我是第%s行\n" % (count,))
#     count += 1
# #     time.sleep(1)
# def func_g(num = 0):
#     sums = 0
#     day = 0
#     avg = 0
#     while True:
#         yield avg  # 返回avg，并接受seed传进来的money
#           # sums = sums + money
#         # day += 1
#         avg += 1
#         # avg = sums/day
#
#
# g = func_g()
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))

# li = [i for i in range(10) if i % 2 == 0]
# lst = []
# for i in range(10):
#     if i % 2 == 0:
#         lst.append(i)
# print(lst)

# li1 = [lambda x: x*i for i in range(10) if i % 2 == 0]
#
# lst = []
# for i in range(10):
#     if i % 2 == 0:
#         lst.append(lambda x: x*i)
# lst = [lambda x: x*i,lambda x: x*i,lambda x: x*i,lambda x: x*i]
#
# li2 = [2 for m in range(5)]
# lst1 = []
# for i in range(5):
#     lst1.append(2)

# def multipliers():
#     return [lambda x:i*x for i in range(4)]
#
# print([m(2) for m in multipliers()])

# def multipliers():
#     lst = []
#     for i in range(4):
#         lst.append(lambda x:i*x)
#     return lst
# lst = multipliers()
# print([m(2) for m in multipliers()])
#
# lst1 = []
# for m in lst:
#     m = lambda x:3*x
#     m(2)

# def multipliers():
#     return (lambda x: i*x for i in range(4))
#
# print([m(2) for m in multipliers()])
#
# # [6,6,6,6]
# def multipliers():
#     lst = [lambda x: i * x,lambda x: i * x,]
#
#
#     i = 2
#     lst.append(lambda x: i * x)
#     i = 3
#     def func(x):
#         return i * x
#     return lst
#
#
# print([m(2) for m in multipliers()])
# lst = []
# for m in multipliers(): # multipliers = lst
#     lst.append(m(2))

# a = "123"
# lst = []
# for i in range(5):
#     lst.append(a)
# print(lst)
# def fun(n):
#     print(n)
#     n += 1
#     fun(n)
# fun(1)
# 6 * 5 * 4 * 3 * 2 *1

# def fn(n):
#     if n == 1:return 1
#     return n*fn(n-1)
# print(fn(6))

# def fn(n):
#     if n == 1:return 1
#     return n * fn(n-1)
# print(fn(6))

# def func(x):
#     if x % 2 == 0:
#         return x
# res = filter(func,[i for i in range(10)])
# print(list(res))
# li = [1, 2, 3, 4]
# # li.index(10)
# try:
#     li.index(10)
# except ValueError:
#     print("列不存在！")


#
# def func1(cmd):
#     print("我是func1", cmd)
#     dic = {1:2,
#            2:3,
#            3:4}
#     return dic
#
# def func3(data):
#     for i in data:
#         print(i)
#
# def func2():
#     cmd = input(">>>:")
#     res = func1(cmd)
#     func3(res)
#
# func2()
# def func():
#     with open("test.py") as f1:
#         for i in f1:
#             yield i
# res = func()
# res1 = res.__next__()
# res2 = res.__next__()
#
# print(res1)
# print(res2)

# def wrapper(func):
#     def inner(*args, **kwargs):
#         print("我是wrapper")
#         res = func(*args, **kwargs)
#         if res != None:
#             return res
#     return inner
#
# @wrapper  # func = wrapper(func)
# def func(argv):
#     print(argv)
#     return argv
# res = func("func")
# print(res)

# def wrapper1(func): # func = inner2
#     def inner1(*args, **kwargs):
#         print("我是第一个wrapper1")
#         res = func(*args, **kwargs) # func = inner2
#         print("我是第二个wrapper1")
#         return res
#     return inner1
#
#
# def wrapper2(func): # func = f1
#     def inner2(*args, **kwargs):
#         print("我是第一个wrapper2")
#         res = func(*args, **kwargs)  # func = f1
#         print("我是第二个wrapper2")
#         return res
#     return inner2
#
# @wrapper1  # f1 = wrapper1(f1) = wrapper1(inner2) = inner1
# @wrapper2  # f1 = wrapper2(f1) = inner2
# def f1(argv):
#     print("我是func!!!")
# f1("参数")  # f1 = inner1
# FLAG = True
#
# def outer(FLAG):
#     def wrapper(func):
#         def inner(*args, **kwargs):
#             if FLAG == True:
#                 print("我是装饰器")
#                 res = func(*args, **kwargs)
#                 return res
#             elif False == False:
#                 res = func(*args, **kwargs)
#                 return res
#         return inner
#     return wrapper
#
# @outer(FLAG)
# def func():
#     print("我是func")
#
# func()

# lst = [[1, 2, 3], ["alex", "spf", "wxx"], ["IT", "UI", "py"]]
# res = zip(*lst)
# for i in res:
#     print(i)

dic = {'id': ['1', '2', '3'],
        'name': ['Alex', 'Egon', 'nezha'],
         'age': ['22', '23', '25'],
         'phone': ['13651054608', '13304320533', '1333235322'],
        'job': ['IT', 'Tearcher', 'IT']}

res = zip(*dic.values())
for i in res:
    print(i)