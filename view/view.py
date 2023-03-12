from PyQt5 import QtCore, QtGui, QtWidgets
from ErrorViewerGui.view.ErrorViewer import Ui_Dialog
class MainView(QtWidgets.QDialog):
    def __init__(self, model, main_controller):
        super(MainView, self).__init__()
        self._model = model
        self._main_controller = main_controller
        self._ui = Ui_Dialog()
        self._ui.setupUi(self)

        # initialize combo box
        websiteList = self.GetWebsites()
        for website in websiteList:
            self._ui.comboBox.addItem(website)


    def GetWebsites(self):
        self._main_controller.getWebsites()
        websiteList = self._model.websiteList
        return websiteList

    def GetErrors(self):
        # get website from combobox
        website = self._ui.comboBox.currentText()
        # controller sets 'resultsStr' property in model
        self._main_controller.GetErrors(website)
        resultsStr = self._model.resultsStr
        # resultsStr value is displayed in textEdit box
        self._ui.errorResultsEdit.setPlainText(resultsStr)