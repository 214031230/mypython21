#!/usr/bin/env python
# -*- coding:utf-8 -*-

from multiprocessing import Queue,Process

def func(q,num):
    try:
        t = q.get_nowait()
        print("%s抢到票了"%num)
    except:pass

if __name__ == '__main__':
    q = Queue()
    q.put(1)
    for i in range(10):
        Process(target=func,args=(q,i)).start()


# 管道 + 锁  == 队列
# 管道也是一个可以实现进程之间通信的模型
# 但是管道没有锁，数据不安全

# 消息中间件
# memcache
# rabitmq
# kafka —— 大数据相关
# redis

