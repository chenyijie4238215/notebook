# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: cyj
@time: 2016/11/21
"""
from PyQt5.QtCore import QUrl

from lantern.QmlWindow import QmlWindow


class MainWindow(QmlWindow):
    def _onCreateView(self):
        self.setSource(QUrl("../qml/MainWindow.qml"))