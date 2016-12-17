# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: cyj
@time: 2016/11/21
"""
from PyQt5.QtCore import QUrl

from QmlWindow import QmlWindow
from presenter.YellowPresenter import YellowPresenter

class YellowWindow(QmlWindow):
    def _onCreateView(self):
        self.setSource(QUrl("./qml/test2.qml"))
        YellowPresenter(self,self.rootObject())

