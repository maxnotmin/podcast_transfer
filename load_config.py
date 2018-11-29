import os, sys
import configparser

Config = configparser.ConfigParser()
loaded_config = Config.read('podcasts.ini')

def ConfigSectionMap(section):
    dict1 = {}
    options = Config.options(section)
    for option in options:
        try:
            dict1[option] = Config.get(section, option)
            if dict1[option] == -1:
                DebugPrint("skip: %s" % option)
        except:
            print("exception on %s!" % option)
            dict1[option] = None

    return dict1

def load_section():
    SHOW_RSS = []
    for show in Config.sections():
        sec = ConfigSectionMap(show)
        SHOW_RSS.append(sec)

    return SHOW_RSS
