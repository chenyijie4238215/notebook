# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: cyj
@time: 2016/11/21
"""
import sys
from PyQt5.QtWidgets import QApplication

from lantern.WindowManager import WindowManager


def main():
    app = QApplication(sys.argv)

    WindowManager.creatAndShow()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()