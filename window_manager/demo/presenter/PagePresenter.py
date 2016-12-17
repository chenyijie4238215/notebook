# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: cyj
@time: 2016/11/22
"""
from Presenter import Presenter

class PagePresenter(Presenter):
    def _onCreatView(self):
        self.view.move.connect(self.window.onMove)
        self.view.closeClicked.connect(self.window.close)
        self.view.yellowPage.connect(self.window.pushYellowPage)
        self.view.redPage.connect(self.window.pushRedPage)
        self.view.bluePage.connect(self.window.pushBluePage)