#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import os
from logging import debug,info,warning,exception,error
from PyQt5 import QtCore
from PyQt5.QtCore import qInstallMessageHandler

def handler(qtMsgType, context, msg):
    # print msg
    # msg = "%s(line:%s):%s" %(context.file,context.line,msg)
    if qtMsgType == QtCore.QtDebugMsg:
        logging.debug(msg)
    elif qtMsgType == QtCore.QtInfoMsg or qtMsgType == QtCore.QtSystemMsg:
        logging.info(msg)
    elif qtMsgType == QtCore.QtWarningMsg:
        logging.warning(msg)
    elif qtMsgType == QtCore.QtCriticalMsg:
        logging.critical(msg)
    elif qtMsgType == QtCore.QtFatalMsg:
        logging.error(msg)
    else:
        logging.exception(msg)

def init(path=r"app.log"):
    if os.path.exists(path):
        os.remove(path)
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s %(levelname)s %(filename)s[line:%(lineno)d] :: %(message)s',
        datefmt='%a, %d %b %Y %H:%M:%S',
        filename=path,
        filemode='a')

    console = logging.StreamHandler()
    level = logging.DEBUG
    console.setLevel(level)
    formatter = logging.Formatter(fmt='%(levelname)s %(filename)s[line:%(lineno)d] :: %(message)s')
    console.setFormatter(formatter)
    logging.getLogger().addHandler(console)

    qInstallMessageHandler(handler)


