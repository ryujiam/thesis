import ConfigParser

class Configured:
    def __init__(self, conf):
        self.setConf(conf)

    def setConf(self, conf):
        self.conf = conf



if __name__ == '__main__':
    conf = Configured(0)
