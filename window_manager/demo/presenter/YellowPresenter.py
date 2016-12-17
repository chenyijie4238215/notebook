from Presenter import Presenter
from WindowManager import WindowManager
from config import Config

class YellowPresenter(Presenter):
    def _onCreatView(self):
        self.view.crateRed.connect(self.onCrateRed)
        self.view.closeWindow.connect(self.window.close)

    def onCrateRed(self):
        WindowManager.windowCreatMode = Config.windowCreatMode
        WindowManager().creatAndShow(Config.RedWindow)