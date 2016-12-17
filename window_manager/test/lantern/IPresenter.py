# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: cyj
@time: 2016/11/21
"""

import sys
from PyQt5.QtCore import QObject
from PyQt5.QtQuick import QQuickItem
from rx.disposables.disposable import Disposable

class IPresenter(QObject):
    """
        IPresenter类或其子类，在实例化时，不应该指定任何变量来对其引用，否则容易内存泄露。
        比如：a = IPresenter() 是不应该的。 直接 IPresenter()
        不需要重写__init__函数，业务逻辑在重载_onCreatView中实现
        """
    def __init__(self, window, view, *model):
        QObject.__init__(self, None)
        self.disposes = {}
        self.window = window
        self.view = view
        self.models = model
        self.window.registerPresenter(self)
        self._onCreatView()

        if isinstance(self.view, QQuickItem) and hasattr(self.view, "destroyed"):
            self.view.destroyed.connect(self.onWindowExit)

    def onWindowExit(self):
        self._releaseAllDispose()
        self._onExitWindow()
        self.window.unRegisterPresenter(self)
        self.window = None
        self.view = None

    def _releaseAllDispose(self):
        for (k, v) in self.disposes.items():
            # if v:
            if isinstance(v, Disposable):
                v.dispose()
        self.disposes.clear()

    def _onCreatView(self):
        pass

    def _onExitWindow(self):
        pass

    def autoReleaseDisposable(self, disposable, disposeKey=None, autoReleaseLaster=True):
        '''
        :param disposable:需要自动释放的对象
        :param disposeKey: 自动释放保存的key  默认为调用此接口的方法名
        :param autoReleaseLaster: 是否自动释放上一个重复的dispose对象,默认为自动释放
        :return:
        '''
        if disposable is not None and hasattr(disposable, 'dispose'):
            disposeKey = disposeKey or sys._getframe().f_back.f_code.co_name  # 获取调用函数名
            try:
                if autoReleaseLaster:
                    self.releaseDisposable(disposeKey)
            except Exception, ex:
                print "autoRelease 自动销毁上一个失败：%s",ex
            self.disposes[disposeKey] = disposable

    def releaseDisposable(self, disposeKey):
        last = self.disposes.pop(disposeKey, None)
        if last is not None and isinstance(last, Disposable):
            print "重复链接同一个disposable，断开上一个,并主动释放"
            last.dispose()