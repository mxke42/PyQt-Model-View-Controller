from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSlot
from ErrorViewerGui.view.ErrorViewer import Ui_Dialog
class MainView(QtWidgets.QDialog):
    def __init__(self, model, main_controller):
        super(MainView, self).__init__()
        self._model = model
        self._main_controller = main_controller
        self._ui = Ui_Dialog()
        self._ui.setupUi(self)

        # listen for model event signals
        self._model.resultsStrChanged.connect(self.onResultsChanged)
        self._model.websitesChanged.connect(self.onWebsitesChanged)

        # initialize combo box
        self.GetWebsites()


    def GetWebsites(self):
        self._main_controller.getWebsites()

    def GetErrors(self):
        # get website from combobox
        website = self._ui.comboBox.currentText()
        # controller sets 'resultsStr' property in model
        self._main_controller.GetErrors(website)

    @pyqtSlot(str)
    def onResultsChanged(self, value):
        self._ui.errorResultsEdit.setPlainText(value)

    @pyqtSlot(list)
    def onWebsitesChanged(self, websiteList):
        for website in websiteList:
            self._ui.comboBox.addItem(website)
