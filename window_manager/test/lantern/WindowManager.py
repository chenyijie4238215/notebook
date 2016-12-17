# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: cyj
@time: 2016/11/21
"""
from PyQt5.QtCore import QObject

class WindowManager(QObject):
    # 标准创建模式，每次创建都是新建一个窗口实例
    STANDAR = 0
    # 如果已经存在相同winName的窗口实例，则直接使用那一个旧的
    SINGLETON_BY_WINNAME = 1
    # 如果已经存在相同winName的窗口实例，则退出那一个旧的窗口，再创建一个新的
    RECREAD_BY_WINNAME = 2

    winDist = {}
    windowCreatMode = {}

    # 单例
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super(WindowManager, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def creatAndShow(self, windowClassName, winName=None, *args, **kwargs):
        """
        创建并显示窗口，根据windowCreatMode和winName综合判断
        :param windowClassName: 目标窗口类（包含完整包名）
        :param winName: 标识本窗口名称的字符串。与mainifest中的windowCreatMode配合使用，决定窗口的创建模式。
        :param args: 窗口子类可以追加的其他参数
        :param kwargs: 窗口子类可以追加的其他参数
        :return:
        """
        wname = str(windowClassName) if winName is None else str(windowClassName + ":" + winName)
        mode = WindowManager.windowCreatMode.get(windowClassName)
        if mode is None:
            mode = WindowManager.STANDAR
        instance = None

        if mode == WindowManager.SINGLETON_BY_WINNAME:
            if WindowManager.winDist.has_key(wname):
                instance = WindowManager.winDist.get(wname)
            else:
                instance = self.createInstance(windowClassName, *args, **kwargs)
                WindowManager.winDist[wname] = instance
                instance.exit.connect(self.onExit)
        elif mode == WindowManager.RECREAD_BY_WINNAME:
            if WindowManager.winDist.has_key(wname):
                instance = WindowManager.winDist.get(wname)
                instance.close()
            instance = self.createInstance(windowClassName, *args, **kwargs)
            instance.exit.connect(self.onExit)
            WindowManager.winDist[wname] = instance
        else:
            instance = self.createInstance(windowClassName, *args, **kwargs)
            instance.exit.connect(self.onExit)

        instance.classAndWinname = wname
        instance.show()
        instance.activateWindow()

        # from app.manifest import manifest
        # title = manifest.windowTitle.get(windowClassName, "来战")
        # print 'title ---->', title
        # instance.setWindowTitle(title)

    def createInstance(self,windowClassName, *arg, **kwargs):
        if len(windowClassName) > 0:
            classNames = windowClassName.split(".")
            pack = ""
            for s in classNames[:-1]:
                pack += s + "."
            pack = pack[:-1]
            # exec语句用来执行储存在字符串或文件中的Python语句
            exec ("import " + str(pack))
            cmd = windowClassName + "(*arg,**kwargs)"
            #eval参数是一个字符串，可以把这个字符串当成表达式来求值。
            inst = eval(str(cmd))
            return inst

    def onExit(self, classAndWinname):
        try:
            print "WindowManager:onExit->%s begin", classAndWinname
            if WindowManager.winDist.has_key(str(classAndWinname)):
                del WindowManager.winDist[str(classAndWinname)]
            print "WindowManager:onExit->%s end", classAndWinname
        except Exception, e:
            print e.message

    def closeWindow(self, windowClassName, winName=None):
        wname = str(windowClassName) if winName is None else str(windowClassName + ":" + str(winName))
        if WindowManager.winDist.has_key(wname):
            del WindowManager.winDist[wname]
        else:
            print 'no such window key:' + wname

    def findWindow(self, windowClassName, winName=None):
        wname = str(windowClassName) if winName is None else str(windowClassName + ":" + winName)
        if WindowManager.winDist.has_key(wname):
            return WindowManager.winDist[wname]
        return None

    def filterAndCloseOther(self,windowList):
        keys = WindowManager.winDist.keys()[0:]
        for wname in keys:
            if wname in windowList:
                continue
            self.closeWindow(wname)