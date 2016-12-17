# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: cyj
@time: 2016/11/21
"""
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtQuickWidgets import QQuickWidget

class QmlWindow(QQuickWidget):
    exit = pyqtSignal(str)
    def __init__(self):
        """
        不要显式地实例化 AbsWindow类及其子类，
        应该通过 WindowManager的 creatAndShow（）方法去创建一个窗口实例,并显示。
        一般不需要重载__init__方法。业务逻辑在重载_onCreatView中实现
        """
        QQuickWidget.__init__(self)
        self.presenters = []
        self.classAndWinname = None
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setStyleSheet("background:transparent;")
        self._onCreateView()


    def closeEvent(self, *args, **kwargs):
        self.exit.emit(self.classAndWinname)
        self.clearPresenters()
        self.deleteLater()

    def registerPresenter(self, presenter):
        if presenter not in self.presenters:
            self.presenters.append(presenter)

    def unRegisterPresenter(self, presenter):
        if presenter in self.presenters:
            print "remove presenter"
            self.presenters.remove(presenter)

    def clearPresenters(self):
        count = len(self.presenters) - 1
        tmp = self.presenters[0: len(self.presenters)]
        while count >= 0:
            p = tmp[count]
            p.onWindowExit()
            count -= 1
        self.presenters = []

    def _onCreateView(self):
        """
        重载以实现自定义控件的内部逻辑。
        """
        pass
