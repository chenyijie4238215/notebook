# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: cyj
@time: 2016/12/9
"""
from PyQt5.QtCore import QStandardPaths, QDir, QUrl
from PyQt5.QtNetwork import QNetworkDiskCache, QNetworkAccessManager
from PyQt5.QtQml import QQmlNetworkAccessManagerFactory


class NetworkAccessManagerFactory(QQmlNetworkAccessManagerFactory):
    def __init__(self):
        QQmlNetworkAccessManagerFactory.__init__(self)

    def create(self, parent):
        nam = QNetworkAccessManager(parent)
        diskCache = QNetworkDiskCache(nam)
        cachePath = QStandardPaths.displayName(QStandardPaths.CacheLocation)
        print "cache path:", cachePath
        diskCache.setCacheDirectory(cachePath)
        diskCache.setMaximumCacheSize(100 * 1024 * 1024)  # 设置100M缓存
        nam.setCache(diskCache)
        return nam


if __name__=="__main__":
    import sys
    from PyQt5.QtWidgets import QApplication
    from PyQt5.QtQuickWidgets import QQuickWidget
    app = QApplication(sys.argv)
    widget = QQuickWidget()
    factory = NetworkAccessManagerFactory()
    widget.engine().setNetworkAccessManagerFactory(factory)
    widget.setSource(QUrl("test.qml"))
    widget.show()
    sys.exit(app.exec_())