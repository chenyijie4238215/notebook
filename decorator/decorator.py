# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: cyj
@time: 2016/11/19
"""

# 打印函数执行时间
def print_exec_time(func):
    import time
    def wrap(*a, **kw):
        start_time = time.time()
        ret = func(*a, **kw)
        print "%s exec time: %s" % (func.__name__, time.time() - start_time)
        return ret
    return wrap

#  打印函数执行线程
def print_exec_thread(func):
    import threading
    def wrap(*a, **kw):
        print "exec %s start -----thread:%s------traceback:%s----------"%\
              (func.__name__, threading.currentThread().getName(), detailtrace(func.__name__))
        ret = func(*a, **kw)
        print "exec %s end   -----thread:%s------traceback:%s----------"%\
              (func.__name__, threading.currentThread().getName(), detailtrace(func.__name__))
        return ret
    return wrap

# 单例装饰器
def singleton(cls):
    instances = dict() # 初始为空
    def _singleton(*args, **kwargs):
        if cls not in instances: #如果不存在, 则创建并放入字典
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return _singleton