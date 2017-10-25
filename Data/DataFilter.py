import pandas as pd
from Conf.Configuration import Configuration
from context.DataContext import DataContext
#from DOC.doc import Doc

class DataFilter:
    def __init__(self, context):
        self.context = context

    def setup(self):
        self.conf = self.context.getConf()
        self.dataModel = self.context.getDataModel()


    def filter(self):
        self.setup()
        colName = self.conf.get("filter", "name")
        subsetName = self.conf.get("filter", "subsetName")
        self.dataFilter = self.dataModel[self.dataModel[colName] == subsetName]

        return self.dataFilter
        print self.dataModel


    def userItemFilter(self, numUser, numItem):
        filterUserNum = self.conf.get("filter", "userNumber")
        filterItemNum = self.conf.get("filter", "itemNumber")
        iterStep = self.conf.get("iter", "step")

    def getDataFilter(self):
        return self.dataFilter




if __name__ == '__main__':
    conf = Configuration("/Users/sakamotoryuuji/Dropbox/thesis/python/resource/config.ini")
