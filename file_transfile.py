import sys
import os
import paramiko
import configparser
import time
import datetime


class TransferFile():
    """

    """

    def __init__(self):
        self.podcast_dir = None
        self.ab_path = os.path.abspath(__file__)
        self.cur_dir = os.getcwd()
        self.podcast_episode = None
        self.podcast_dir = None
        self.podcast_ab_path_episode = None
        self.target_host = None
        self.target_port = None
        self.target_auth = None


    def load_podocast_config(self):
        pass

    def load_server_congif(self):
        pass

    def create_path_to_episode(self):
        pass



