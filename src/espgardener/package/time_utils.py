import time

def getTimeStamp():
    return("{:4d} {:02d} {:02d} {:02d}:{:02d}:{:02d}".format(*time.localtime()))