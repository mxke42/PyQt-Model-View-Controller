from PyQt5.QtCore import QObject, pyqtSlot
from MySqlClass import MySqlDatabase
from MongoDatabaseClass import MongoDatabase

# functions to grab data and store in model

class MainController(QObject):

    def __init__(self, model):
        super().__init__()
        self._model = model

    def getWebsites(self):

        MySqlDatabase.initialize()
        cursor = MySqlDatabase.connection.cursor()
        queryStr = "SELECT example FROM example.example_websites"
        cursor.execute(queryStr)
        websiteList = []
        for website in cursor:
            websiteList.append(website[0])
        self._model.websiteList = websiteList

    def GetErrors(self, website):
        # check connection
        if not MongoDatabase.connectionActive:
            MongoDatabase.initialize()
        # get result of query
        resultsStr = MongoDatabase.search("example", website)
        if resultsStr == "":
            resultsStr = "No errors"
        self._model.resultsStr = resultsStr
