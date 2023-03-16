from PyQt5.QtCore import QObject, pyqtSignal, QAbstractListModel
#import PyQt5


class Model(QObject):
    resultsStrChanged= pyqtSignal(str)
    websitesChanged = pyqtSignal(list)
    def __init__(self):
        super().__init__()

    @property
    def websiteList(self):
        return self._websiteList

    @property
    def resultsStr(self):
        return self._resultsStr

    @websiteList.setter
    def websiteList(self, value):
        self._websiteList = value
        self.websitesChanged.emit(value)

    @resultsStr.setter
    def resultsStr(self, value):
        self._resultsStr = value
        self.resultsStrChanged.emit(value)




