from abc import ABCMeta, abstractmethod

class AbstractContext(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def __init__(self):
        pass


    def setConf(self, conf):
        self.conf = conf

    def getConf(self):
        return self.conf


