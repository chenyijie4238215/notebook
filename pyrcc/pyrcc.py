# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: cyj
@time: 2016/11/19
"""
import os

pyrcc = "pyrcc5"                    #打包程序
rootDir = "temp/t1"                 #资源文件夹
filterType = ["qml", "js", "html"]  #资源类型过滤

qrcPath = "resource.qrc"            #资源清单文件名
rccPath = "resource.py"             #资源文件名

def create_qrc():
    qrcFiles = ""
    for parent, dirnames, filenames in os.walk(rootDir):
        for filename in filenames:
            path = os.path.join(parent, filename)
            if path.split('.')[-1].lower() in filterType:
                path = path.replace("\\",'/')
                qrcFile = "<file>%s</file>\n" % path
                qrcFiles += qrcFile
    qrc = "<RCC>\n<qresource prefix=\"/\">\n%s</qresource>\n</RCC>" % qrcFiles
    file = open(qrcPath, 'w')
    file.write(qrc)
    file.close()
    os.system("%s  %s -compress 9 -o %s" % (pyrcc, qrcPath, rccPath))

if __name__ == '__main__':
    create_qrc()