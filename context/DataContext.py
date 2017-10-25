from context.AbstractContext import AbstractContext

class DataContext(AbstractContext):
    def __init__(self, conf, dataModel):
        self.conf = conf
        self.dataModel = dataModel

    def getDataModel(self):
        return self.dataModel
