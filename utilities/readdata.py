import configparser
import os

config = configparser.RawConfigParser()
config.read(os.path.abspath(os.curdir)+'\\configuration\\config.ini')

class ReadData:

    @staticmethod
    def getbaseurl():
        url=(config.get('testdata','baseurl'))
        return url

    @staticmethod
    def getuserid():
        userid=(config.get('testdata','userid'))
        return userid

    @staticmethod
    def getpwd():
        pwd=(config.get('testdata','pwd'))
        return pwd
