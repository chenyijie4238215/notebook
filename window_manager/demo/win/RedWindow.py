# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: cyj
@time: 2016/11/21
"""
from PyQt5.QtCore import QUrl

from QmlWindow import QmlWindow
from presenter.RedPresenter import RedPresenter


class RedWindow(QmlWindow):
    def _onCreateView(self):
        self.setSource(QUrl("./qml/test1.qml"))
        RedPresenter(self,self.rootObject())

