# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: cyj
@time: 2016/11/19
"""

def print_exec_time(func):
    import time
    def wrap(*a, **kw):
        start_time = time.time()
        ret = func(*a, **kw)
        print "%s exec time: %s" % (func.__name__, time.time() - start_time)
        return ret
    return wrap

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
