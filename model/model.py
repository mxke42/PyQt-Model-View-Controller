from PyQt5.QtCore import QObject, pyqtSignal, QAbstractListModel
#import PyQt5



class Model(QObject):
    def __init__(self):
        super().__init__()
        # self._websiteList = None
        # self._resultsStr = None

    @property
    def websiteList(self):
        return self._websiteList

    @property
    def resultsStr(self):
        return self._resultsStr

    @websiteList.setter
    def websiteList(self, value):
        self._websiteList = value

    @resultsStr.setter
    def resultsStr(self, value):
        self._resultsStr = value



