# !/usr/bin/python2
# coding: utf-8

import sys
# import logging
from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5.QtCore import qInstallMessageHandler, QUrl
from PyQt5.QtQuickWidgets import QQuickWidget
import logger

def handler(qtMsgType, qMessageLogContext, msg):
    # print msg
    logging.basicConfig(level=logging.DEBUG)
    if qtMsgType == QtCore.QtDebugMsg:
        # logging.debug(msg)
        logging.info(msg)
    elif qtMsgType == QtCore.QtInfoMsg or qtMsgType == QtCore.QtSystemMsg:
        logging.info(msg)
    elif qtMsgType == QtCore.QtWarningMsg:
        logging.warning(msg)
    elif qtMsgType == QtCore.QtCriticalMsg:
        logging.critical(msg)
    elif qtMsgType == QtCore.QtFatalMsg:
        logging.error(msg)
        logging.exception(msg)
    else:
        logging.error(msg)

class HelloWorld(QtWidgets.QWidget):
    def __init__(self,parent = None):
        super(HelloWorld,self).__init__()#使用super()方法继承父类
        self.resize(250, 150)               #改变窗口部件的大小
        self.setWindowTitle('Hello Word!')  #设置窗口部件标题

class QmlWidget(QQuickWidget):
    def __init__(self):
        self.setSource(QUrl("test.qml"))

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    # qInstallMessageHandler(handler)
    # helloworld = HelloWorld()
    # helloworld.show()
    logger.init()
    view = QQuickWidget()
    view.setSource(QUrl.fromLocalFile("temp/test.qml"))
    view.show()
    sys.exit(app.exec_())