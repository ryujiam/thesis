import ConfigParser
import os
import sys
class Configuration:
    def __init__(self, name):
        self.inifile = ConfigParser.SafeConfigParser()
        self.inifile.read("/Users/sakamotoryuuji/Dropbox/thesis/python/resource/default.ini")
        if os.path.exists(name):
            self.inifile.read(name)
        else:
            sys.stderr.write('%s' % name)
            sys.exit(2)



    def get(self, name, value):
        return self.inifile.get(name, value)


if __name__ == '__main__':
    configuration = Configuration("/Users/sakamotoryuuji/Dropbox/thesis/python/resource/config.ini")
    print configuration.get("doc", "splitWord")

