import os, sys
import paramiko
import configparser
from ftplib import FTP

#TODO
#Create a config class to unify the INI reading. Perhaps move the INI loading to MAIN.py

#LOAD SERVER CONFIG
Config = configparser.ConfigParser()
loaded_config = Config.read('server_info.ini')

def ConfigSectionMap(section):
    dict1 = {}
    options = Config.options(section)
    for option in options:
        print("OPTIONS: ", option)
        try:
            dict1[option] = Config.get(section, option)
            if dict1[option] == -1:
                DebugPrint("skip: %s" % option)
        except:
            print("exception on %s!" % option)
            dict1[option] = None

    return dict1

def load_section():
    SERVER_HOLDER = []
    for show in Config.sections():
        print("SHOW", show)
        sec = ConfigSectionMap(show)
        SERVER_HOLDER.append(sec)

    return SERVER_HOLDER

radio_co = load_section()
print("RadioCo: ", radio_co)

def transfer_file_to_ftp(localfilepath='',remotefilepath=''):
    try:
        print("STARTING TRANSPORT")
        # Open a transport
        transport = paramiko.Transport((radio_co[0]['host'], int(radio_co[0]['port'])))
        # Auth
        print("STARTING FTP AUTH")
        transport.connect(username=radio_co[0]['username'] ,password=radio_co[0]['pass'])
        print("STARTING SFTP TRANS")

        sftp = paramiko.SFTPClient.from_transport(transport)
        sftp.put(localfilepath,remotefilepath)
        sftp.close()
    except Exception as e:
        print("transfer_file_to_ftp ERROR: ", str(e))



loc_path = 'our_big_dumb_mouth/OBDM660.mp3'
remote_path = ''

#transfer_file_to_ftp(localfilepath=loc_path, remotefilepath=remote_path)

def ftp_transfer_episode(localfilepath='',remotefilepath='', filename=''):
    ftp_con = FTP(host=radio_co[0]['host'])
    ftp_con.login(user=radio_co[0]['username'], passwd=radio_co[0]['pass'])
    dir_content = ftp_con.retrlines('LIST')
    print("FTP DIR: ", str(dir_content))
    #transfer mp3
    try:
        the_mp3 = open(localfilepath, 'rb')
        remote_file = 'STOR {episode}'.format(episode=filename)
        ftp_con.storbinary(remote_file, the_mp3)
        ftp_con.quit()
        ftp_con.close()
    except Exception as FTP_ERROR:
        print("FTP TRANS ERROR: ", str(FTP_ERROR))
        ftp_con.quit()
        ftp_con.close()


ftp_transfer_episode(localfilepath=loc_path, filename='OBDM660.mp3')