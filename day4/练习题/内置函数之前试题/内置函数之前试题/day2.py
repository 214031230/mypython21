# #!/usr/bin/env python3
#
# 1. 列举字典的10种常用方法
# 2. 列举元组的10种常用方法
# 3. 列举集合的10种常用方法
# 4. 判断"yuan"是否在[123,(1,"yuan"),{"yuan":"handsome"},"yuanhao"],如何判断以及对应结果？
# lst = [123,(1,"yuan"),{"yuan":"handsome"},"yuanhao"]
#
# def func(argv):
#     for i in argv:
#         if type(i) == str or type(i) == int:
#             if i == "yuan":
#                 print("找到yuan")
#         else:
#             func(i)
# func(lst)




# # 5.
# i = ['name', 'age']
# l = ['金鑫', 58]
# print(dict([i, l]))
# print(dict([i, l]))
# {“name”:"金鑫","age":18}
# 	请用代码实现结果{“name”:"金鑫","age":18}
# def func(argv):
#     dic = {}
#     dic[argv[0]] = argv[1]
#     return dic
# print(list(map(func,zip(i, l))))


# 6. range和xrange的区别，以及各自的应用场景
# print(dir(range(10)))
# 7.  v1 = {}
# 	v2 = {3:5}
# 	v3 = {[11,23]:5}  # 字典的key必须是可哈希的，可哈希=不可变
# 	v4 = {(11,23):5}
# 	下面代码谁报错？
# 8.将字符串："k:1|k1:2|k2:3|k3:4"，处理成 python 字典：{k:1, k1:2, ... }
# s = "k:1|k1:2|k2:3|k3:4"
# lst = [i.split(":") for i in s.split("|")]
# # print(lst)
# print(dict([*lst]))
#
#
# 9. 有如下变量（tu是个元祖），请实现要求的功能
#     tu = ("alex", [11, 22, {"k1": 'v1', "k2": ["age", "name"], "k3": (11,22,33)}, 44])
#     a. 讲述元祖的特性
#       只读列表
#     b. 请问tu变量中的第一个元素 “alex” 是否可被修改？
#       不可修改
#     c. 请问tu变量中的"k2"对应的值是什么类型？是否可以被修改？如果可以，请在其中添加一个元素 “Seven”
#       列表
# tu = ("alex", [11, 22, {"k1": 'v1', "k2": ["age", "name"], "k3": (11,22,33)}, 44])
# tu[1][2]["k2"].append("Seven")
# print(tu)
# 	d. 请问tu变量中的"k3"对应的值是什么类型？是否可以被修改？如果可以，请在其中添加一个元素 “Seven”
#   元组类型，不可修改
#
# # 10. 字典dic,dic = {'k1': "v1", "k2": "v2", "k3": [11,22,33]}
# dic = {'k1': "v1", "k2": "v2", "k3": [11,22,33]}
# #     a. 请循环输出所有的key
# for i in dic.keys():
#     print(i)
# #     b. 请循环输出所有的value
# for i in dic.values():
#     print(i)
# #     c. 请循环输出所有的key和value
# for k, v in dic.items():
#     print(k, v)
# #     d. 请在字典中添加一个键值对，"k4": "v4"，输出添加后的字典
# dic["k4"] = "v4"
# print(dic)
# #     e. 请在修改字典中 “k1” 对应的值为 “alex”，输出修改后的字典
# dic["k1"] = "alex"
#
# #     f. 请在k3对应的值中追加一个元素 44，输出修改后的字典
# dic["k3"].append(44)
# #     g. 请在k3对应的值的第 1 个位置插入个元素 18，输出修改后的字典
# dic["k3"].insert(1, 18)
# print(dic)
# #
# 11. 元素分类
#     有如下值li= [11,22,33,44,55,66,77,88,99,90]，将所有大于 66 的值保存至字典的第一个key中，将小于 66 的值保存至第二个key的值中。
# # 	即： {'k1': 大于66的所有值列表, 'k2': 小于66的所有值列表}
# li= [11,22,33,44,55,66,77,88,99,90]
# dic = {"k1": [],
#        "k2": []}
# for i in li:
#     if i > 66:
#         dic["k1"].append(i)
#     else:
#         dic["k2"].append(i)
# print(dic)
#
#
# 12. 输出商品列表，用户输入序号，显示用户选中的商品
#     商品 li = ["手机", "电脑", '鼠标垫', '游艇']
# 	要求：1：页面显示 序号 + 商品名称，如：
# 	      	1 手机
# 		   	2 电脑
# 	     		 …
# 	     2： 用户输入选择的商品序号，然后打印商品名称
# 	     3：如果用户输入的商品序号有误，则提示输入有误，并重新输入。
# 	     4：用户输入Q或者q，退出程序。
#
# 13.对字典进行增删改查  {"Development":"开发小哥","OP":"运维小哥","Operate":"运营小仙女","UI":"UI小仙女"}
#
# 14. 写一个三次认证 实现用户输入用户名和密码,当用户名为 seven 或 alex 且 密码为 123 时,显示登陆成功,否则登陆失败,失败时允许重复输入三次
#
# 15. 元祖和列表的区别
#
# 16. 从键盘接收一百分制成绩（0~100），要求输出其对应的成绩等级A~E。其中，90分以上为'A'，80~89分为'B'，70~79分为'C'，60~69分为'D'，60分以下为'E'
#
# 17. 深浅copy-引用和copy(),deepcopy()的区别
#
# 18. 自定义两个，并求交集，合集，差集。
#
#
#
#
#
