import sys
import os
import datetime
import time
import paramiko
import feedparser
import requests
import json
import xmltodict
import re
from collections import deque


SHOW_LIST = {
    "obmd":"",
    "grimeria":"",
    "cruzsteak":""
}

THE_FEED = 'http://ourbigdumbmouth.libsyn.com/rss'


def test_get_rss():
    feed_test = feedparser.parse(THE_FEED)
    print("FEED PARSE OBJ: ", feed_test['entries'])
    most_recent = []
    feed_title = feed_test['feed']['title']
    print("FEED TITLE ", feed_title)
    for i in feed_test.entries[0:1]:
        try:
            print("SHOW TITLE: ", i['title'])
            most_recent.append({
                'show_name': feed_title,
                'episode_title': i['title'],
                'episode_mp3': i['links'][1]['href']
            })
        except Exception as e:
            print(e)
    print("LIST: ", most_recent)
    return most_recent


def pod_parse():
    req = requests.get(THE_FEED)
    raw_xml = req.text
    feed_obj = xmltodict.parse(raw_xml)
    print(feed_obj)
    #podcast = Podcast(req.content)
    #print("PODCAST: ", podcast.feed_content)





def download_mp3():
    pass

class CheckFeeds():
    """

    """
    timestr = time.strftime("%Y%m%d-%H%M%S")
    now_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    def __init__(self, feed_url=''):
        self.feed_url = feed_url
        self.feed_obj = None
        self.podcast_name = None
        self.podcast_dir_name = None
        self.podcast_dir_content = None
        self.podcast_obj = None
        self.episode_name = None
        self.episode_pub_date = None
        self.episode_file_name = None
        self.episode_url = None
        self.podcast_ab_path_dir = None
        self.episode_full_path = None
        self.episode_length = None
        self.episode_size = None
        self.ftp_date = None
        self.ab_path = os.path.dirname(os.path.abspath(__file__))
        self.cur_dir = os.getcwd()
        self.rss_load_feed()


    def rss_load_feed(self):
        """
        This function inits all the major attributes used for created the folders and paths
        :return:
        """
        load_feed = feedparser.parse(self.feed_url)
        self.feed_obj = load_feed
        show_title = load_feed['feed']['title']
        self.podcast_name = show_title
        #self.create_dir_name()
        #self.local_make_dir()

        return self

    def create_dir_name(self):
        show_underscrore = self.podcast_name.replace(" ", "_")
        pod_dir_name = show_underscrore.lower()
        self.podcast_dir_name = pod_dir_name
        self.podcast_ab_path_dir = os.path.join(self.ab_path, pod_dir_name)
        return self

    def rss_parse_most_recent(self):
        most_recent = []
        try:
            for i in self.feed_obj.entries[0:1]:

                    print("SHOW TITLE: ", i['title'])
                    most_recent.append({
                        'show_name': self.podcast_name,
                        'episode_title': i['title'],
                        'episode_mp3': i['links'][1]['href']
                    })
            self.podcast_obj = most_recent
            return self
        except Exception as e:
                print(e)




    def rss_check_most_recent_ep(self):
        pass

    def clean_mp3_url(self):
        try:
            clean_url = self.podcast_obj[0]['episode_mp3'].split('?').pop(0)
            self.episode_url = clean_url
            print("CLEAN URL: ", clean_url)
            return self
        except Exception as e:
            print("Clean MP3 Error: ", str(e))


    def create_file_name(self):
        split_url = self.episode_url.split('/')
        print("Splint: ", split_url)
        for word in split_url:
            if '.mp3' in word:
                print("word: ", word)
                self.episode_file_name = word
                complete_file_path = os.path.join(self.podcast_ab_path_dir, word)
                self.episode_full_path = complete_file_path

        return self

    def rss_download_most_recent_ep(self):
        """
        writes the mp3 file to the local directory
        :return:
        """
        local_content = self.local_episodes_list()
        if self.episode_file_name not in self.podcast_dir_content:
            the_mp3_url = self.podcast_obj[0]['episode_mp3']
            print("MP3 URL: ", the_mp3_url)
            req = requests.get(the_mp3_url, stream=True)
            with open(self.episode_full_path, 'wb') as f:
                for chunk in req.iter_content(chunk_size=1024):
                    if chunk:
                        # filter out keep-alive new chunks
                        f.write(chunk)
        else:
            print("MP3 was already downloaded")

    def local_make_dir(self):
        """
        This function will create a directory for your log files if it does not already exist
        :return: None
        """
        if not os.path.exists(self.podcast_dir_name):
            os.makedirs(self.podcast_dir_name)

        return self

    def local_episodes_list(self):
        the_folder = self.podcast_ab_path_dir
        local_episode_holder = []
        for file in os.listdir(the_folder):
            if file.endswith(".mp3"):
                local_episode_holder.append(file)
        print("LOC: ", local_episode_holder)
        self.podcast_dir_content = local_episode_holder
        return self

    def local_get_most_recent_by_date(self):
        pass

    def check_db(self):
        pass

    def write_db(self):
        pass

    def fpt_connect_to_target(self):
        pass

    def ftp_check_items_on_target(self):
        pass

    def send_episode_to_ftp_target(self):
        pass




