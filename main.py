from rss_fetch import CheckFeeds


test_feed_url = 'http://ourbigdumbmouth.libsyn.com/rss'


def run():
    """
    do stuff
    :return:
    """
    print("TEST MAIN |")
    test = CheckFeeds(feed_url=test_feed_url)
    test.rss_parse_most_recent()
    print("SEE DICT: ", test.podcast_obj)

    test.create_dir_name()
    test.local_make_dir()
    print("FULL PATH TO dir ", test.podcast_ab_path_dir)
    test.local_episodes_list()
    print("Local Episodes: ", test.podcast_dir_content)
    test.clean_mp3_url()
    test.create_file_name()
    print(" ATTRIBUTE : ", test.episode_file_name, test.episode_full_path)
    #Write MP3 to local dir
    test.rss_download_most_recent_ep()
    test.local_episodes_list()
    for i in test.podcast_dir_content:
        print(i)


    #test.rss_download_most_recent_ep()



    pass

if __name__ == "__main__":
    run()