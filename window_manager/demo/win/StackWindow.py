# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: cyj
@time: 2016/11/22
"""
from PyQt5.QtCore import QUrl, QObject

from QmlWindow import QmlWindow
from presenter.PagePresenter import PagePresenter


class StackWindow(QmlWindow):
    def _onCreateView(self):
        self.setSource(QUrl("./qml/test3.qml"))
        self.pushYellowPage()
        
    def onMove(self,x,y):
        self.move(self.x()+x,self.y()+y)

    def pushYellowPage(self):
        self.yellowPage = self.rootObject().findChild(QObject, "yellowPage")
        print "yellowPage:", self.yellowPage
        PagePresenter(self,self.yellowPage)

    def pushRedPage(self):
        self.redPage = self.rootObject().findChild(QObject, "redPage")
        print "redPage:", self.redPage
        PagePresenter(self,self.redPage)

    def pushBluePage(self):
        self.bluePage = self.rootObject().findChild(QObject, "bluePage")
        print "redPage:", self.bluePage
        PagePresenter(self,self.bluePage)

