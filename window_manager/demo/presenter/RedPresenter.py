# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: cyj
@time: 2016/11/21
"""

from Presenter import Presenter
from WindowManager import WindowManager
from config import Config

class RedPresenter(Presenter):
    def _onCreatView(self):
        self.view.crateYellow.connect(self.onCrateYellow)
        self.view.closeWindow.connect(self.window.close)

    def onCrateYellow(self):
        WindowManager().creatAndShow(Config.YellowWindow)