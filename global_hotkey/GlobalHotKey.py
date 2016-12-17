# !/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: cyj
@time: 2016/11/30
"""
from ctypes import windll
from ctypes.wintypes import MSG
from win32api import HIWORD, LOWORD

import win32con
from PyQt5.QtCore import QObject, pyqtSignal, Qt, QAbstractEventDispatcher, QTimer, QAbstractNativeEventFilter
from PyQt5.QtGui import QKeySequence


class HotKeyEventFilter(QAbstractNativeEventFilter):
    def __init__(self, hotKey=None):
        QAbstractNativeEventFilter.__init__(self)
        QAbstractEventDispatcher.instance().installNativeEventFilter(self)
        self.hotKey = hotKey
        self.enable = True
        self.count = 0

    def __del__(self):
        QAbstractEventDispatcher.instance().removeNativeEventFilter(self)

    def nativeEventFilter(self, typ, sip_voidptr):
        msg = MSG.from_address(sip_voidptr.__int__())
        if msg.message == win32con.WM_HOTKEY:
            if self.enable is True:
                self.hotKey.setActive(True, HIWORD(msg.lParam), LOWORD(msg.lParam))
            self.count += 1
        return False, 1


class GlobalHotKey(QObject):
    pressed = pyqtSignal()
    released = pyqtSignal()
    register = pyqtSignal(bool)
    unregister = pyqtSignal(bool)

    hotkeyDict = {}

    def __init__(self, shortcut=None):
        QObject.__init__(self)
        self.shortcut = shortcut
        self.nativeKey = 0
        self.nativeMods = 0
        self.count = 0
        self.timer = QTimer()
        self.filter = HotKeyEventFilter(self)
        self.registerShortcut(shortcut)
        self.timer.timeout.connect(self.onTimerout)

    def onTimerout(self):
        if self.filter.count != self.count:
            self.count = self.filter.count
        else:
            self.setActive(False, self.nativeKey, self.nativeMods)

    def setActive(self, active, nativeKey, nativeMods):
        hotkey = self.hotkeyDict.get((nativeKey, nativeMods), None)
        if hotkey is None:
            return
        if active is True:
            hotkey.filter.enable = False
            hotkey.filter.count = 0
            hotkey.count = 0
            hotkey.pressed.emit()
            hotkey.timer.start(240)
        else:
            hotkey.timer.stop()
            hotkey.released.emit()
            hotkey.filter.enable = True

    def registerShortcut(self, shortcut):
        if isinstance(shortcut, QKeySequence):
            allMods = Qt.ShiftModifier | Qt.ControlModifier | Qt.AltModifier | Qt.MetaModifier
            if shortcut.isEmpty():
                return False
            key = (shortcut[0] ^ int(allMods)) & shortcut[0]
            mods = shortcut[0] & int(allMods)
            self.nativeKey = self.nativeKeycode(key)
            self.nativeMods = self.nativeModifiers(mods)
            if windll.user32.RegisterHotKey(0, self.nativeMods ^ self.nativeKey, self.nativeMods, self.nativeKey):
                print "注册热键成功：", shortcut.toString()
                self.hotkeyDict[(self.nativeKey, self.nativeMods)] = self
                self.register.emit(True)
            else:
                print "注册热键失败：", shortcut.toString()
                self.register.emit(False)
        return False

    def unregisterShortcut(self):
        if self.nativeKey is None or self.nativeMods is None:
            return
        if windll.user32.UnregisterHotKey(0, self.nativeMods ^ self.nativeKey):
            print "注销热键成功：", self.shortcut.toString()
            del self.hotkeyDict[(self.nativeKey, self.nativeMods)]
            self.unregister.emit(True)
        else:
            print "注销热键失败：", self.shortcut.toString()
            self.unregister.emit(False)

    def nativeModifiers(self, modifiers):
        native = 0
        if modifiers & Qt.ShiftModifier:
            native |= win32con.MOD_SHIFT
        if modifiers & Qt.ControlModifier:
            native |= win32con.MOD_CONTROL
        if modifiers & Qt.AltModifier:
            native |= win32con.MOD_ALT
        if modifiers & Qt.MetaModifier:
            native |= win32con.MOD_WIN
        return native

    def nativeKeycode(self, key):
        if key == Qt.Key_Escape:
            return win32con.VK_ESCAPE
        elif key in [Qt.Key_Tab, Qt.Key_Backtab]:
            return win32con.VK_TAB
        elif key == Qt.Key_Backspace:
            return win32con.VK_BACK
        elif key in [Qt.Key_Return, Qt.Key_Enter]:
            return win32con.VK_RETURN
        elif key == Qt.Key_Insert:
            return win32con.VK_INSERT
        elif key == Qt.Key_Delete:
            return win32con.VK_DELETE
        elif key == Qt.Key_Pause:
            return win32con.VK_PAUSE
        elif key == Qt.Key_Print:
            return win32con.VK_PRINT
        elif key == Qt.Key_Clear:
            return win32con.VK_CLEAR
        elif key == Qt.Key_Home:
            return win32con.VK_HOME
        elif key == Qt.Key_End:
            return win32con.VK_END
        elif key == Qt.Key_Left:
            return win32con.VK_LEFT
        elif key == Qt.Key_Up:
            return win32con.VK_UP
        elif key == Qt.Key_Right:
            return win32con.VK_RIGHT
        elif key == Qt.Key_Down:
            return win32con.VK_DOWN
        elif key == Qt.Key_PageUp:
            return win32con.VK_PRIOR
        elif key == Qt.Key_PageDown:
            return win32con.VK_NEXT
        elif key == Qt.Key_F1:
            return win32con.VK_F1
        elif key == Qt.Key_F2:
            return win32con.VK_F2
        elif key == Qt.Key_F3:
            return win32con.VK_F3
        elif key == Qt.Key_F4:
            return win32con.VK_F4
        elif key == Qt.Key_F5:
            return win32con.VK_F5
        elif key == Qt.Key_F6:
            return win32con.VK_F6
        elif key == Qt.Key_F7:
            return win32con.VK_F7
        elif key == Qt.Key_F8:
            return win32con.VK_F8
        elif key == Qt.Key_F9:
            return win32con.VK_F9
        elif key == Qt.Key_F10:
            return win32con.VK_F10
        elif key == Qt.Key_F11:
            return win32con.VK_F11
        elif key == Qt.Key_F12:
            return win32con.VK_F12
        elif key == Qt.Key_F13:
            return win32con.VK_F13
        elif key == Qt.Key_F14:
            return win32con.VK_F14
        elif key == Qt.Key_F15:
            return win32con.VK_F15
        elif key == Qt.Key_F16:
            return win32con.VK_F16
        elif key == Qt.Key_F17:
            return win32con.VK_F17
        elif key == Qt.Key_F18:
            return win32con.VK_F18
        elif key == Qt.Key_F19:
            return win32con.VK_F19
        elif key == Qt.Key_F20:
            return win32con.VK_F20
        elif key == Qt.Key_F21:
            return win32con.VK_F21
        elif key == Qt.Key_F22:
            return win32con.VK_F22
        elif key == Qt.Key_F23:
            return win32con.VK_F23
        elif key == Qt.Key_F24:
            return win32con.VK_F24
        elif key == Qt.Key_Space:
            return win32con.VK_SPACE
        elif key == Qt.Key_Asterisk:
            return win32con.VK_MULTIPLY
        elif key == Qt.Key_Plus:
            return win32con.VK_ADD
        elif key == Qt.Key_Comma:
            return win32con.VK_SEPARATOR
        elif key == Qt.Key_Minus:
            return win32con.VK_SUBTRACT
        elif key == Qt.Key_Slash:
            return win32con.VK_DIVIDE
        elif key in [
            Qt.Key_0, Qt.Key_1, Qt.Key_2, Qt.Key_3, Qt.Key_4, Qt.Key_5,
            Qt.Key_6, Qt.Key_7, Qt.Key_8, Qt.Key_9, Qt.Key_A, Qt.Key_B,
            Qt.Key_C, Qt.Key_D, Qt.Key_E, Qt.Key_F, Qt.Key_G, Qt.Key_H,
            Qt.Key_I, Qt.Key_J, Qt.Key_K, Qt.Key_L, Qt.Key_M, Qt.Key_N,
            Qt.Key_O, Qt.Key_P, Qt.Key_Q, Qt.Key_R, Qt.Key_S, Qt.Key_T,
            Qt.Key_U, Qt.Key_V, Qt.Key_W, Qt.Key_X, Qt.Key_Y, Qt.Key_Z
        ]:
            return key
        return 0


if __name__ == "__main__":
    from PyQt5.QtWidgets import QApplication, QWidget
    import sys

    app = QApplication(sys.argv)
    win = QWidget()
    win.resize(400, 400)
    ghk = GlobalHotKey(QKeySequence("Ctrl+F1"))
    ghk.pressed.connect(win.showMaximized)
    ghk.released.connect(win.showNormal)
    # ghk.unregisterShortcut()
    win.show()
    sys.exit(app.exec_())