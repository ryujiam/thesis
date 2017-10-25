import pandas as pd
from Conf.Configured import Configured
from scipy.io import arff
from cStringIO import StringIO
from Conf.Configuration import Configuration
from context.DataContext import DataContext
from Data.DataFilter import DataFilter

class Doc(Configured):

    def read(self):
        inPath = self.conf.get("doc", "inpath")
        splitWord = self.conf.get("doc", "splitWord")
        writeWord = self.conf.get("doc", "writeWord")

        self.dataFile = pd.read_csv(inPath, delimiter=splitWord, engine='python')

    def write(self, dataModel):
        outPath = self.conf.get("doc", "outPath")
        fileOut = open(outPath, 'w')
        for index, row in dataModel.iterrows():
            fileOut.write("<DOC>" + "\n")
            fileOut.write(row['review'] + "\n")
            fileOut.write("</DOC>" + "\n")

    def writeDataFrame(self, dataFrame):
        outPath = self.conf.get("doc", "dfOutPath")
        dataFrame.to_csv(index=False)

    def getData(self):
        return self.dataFile

if __name__ == '__main__':
    conf = Configuration("/Users/sakamotoryuuji/Dropbox/thesis/python/resource/config.ini")
    doc = Doc(conf)
    doc.read()
    df = doc.getData()
    context = DataContext(conf, df)
    config = context.getConf()
    datafilter = DataFilter(DataContext(conf, df))
    datafilter.filter()
    datafil = datafilter.getDataFilter()
    print context.getDataModel()['category'].value_counts()
    print datafil
    doc.write(datafil)

