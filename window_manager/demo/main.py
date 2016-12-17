# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: cyj
@time: 2016/11/21
"""
import sys
from PyQt5.QtWidgets import QApplication

from config import Config
from WindowManager import WindowManager
from logger import logger


def main():
    app = QApplication(sys.argv)
    logger.init()
    WindowManager.windowCreatMode = Config.windowCreatMode
    WindowManager().creatAndShow(Config.StackWindow)

    sys.exit(app.exec_())

if __name__=="__main__":
    main()