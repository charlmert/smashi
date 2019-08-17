# adapted from https://git.styrion.net/iteas/iteas-tools/blob/master/proxmox/proxmox_install_PVE5.py

from datetime import datetime

## TODO: use logging module to log to file
#import logging
## Get an instance of a logger
#logger = logging.getLogger(__name__)

class Logger:
    def __init__(self, filename = '%s' % (__name__)):
        self.f = fr = open(filename, "a+")

    def debug(self, text):
        message = 'DEBUG: %s' % (text)
        self.f.write("%s, %s\n" % (datetime.now(), message))
        print(message)

    def info(self, text):
        message = 'INFO: %s' % (text)
        self.f.write("%s, %s\n" % (datetime.now(), message))
        print(message)

    def error(self, text):
        message = 'ERROR: %s' % (text)
        self.f.write("%s, %s\n" % (datetime.now(), message))
        print(message)

    def close(self):
        self.f.close()
