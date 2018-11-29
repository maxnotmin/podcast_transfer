import os, sys
import json


class JSONPodTracker():
    """
    EXAMPLE TEST:
    test_json = JSONPodTracker(show_name='our_big_dumb_mouth', episode_file_name='OBDM660.mp3')
    test_json.json_load()
    print(test_json.loaded_json)
    test_json.json_check_write_key()
    test_json.json_check_value()

    """
    JSON_FILE_LOC = 'podcast_tracker.json'

    def __init__(self, json_file='podcast_tracker.json', show_name='', episode_file_name=''):
        self.json_file = json_file
        self.show_name = show_name
        self.episode_file_name = episode_file_name
        self.loaded_json = None
        self.updated_json = None
        self.ab_path = os.path.dirname(os.path.abspath(__file__))
        self.cur_dir = os.getcwd()
        self.json_load()

    def json_load(self):
        full_path_to_json = os.path.join(self.ab_path, self.json_file)
        print("FULL JSON PATH: ", full_path_to_json)
        with open(full_path_to_json) as file:
            live_json = json.load(file)
            self.loaded_json = live_json

        return self

    def create_new_list_values(self):

        holder = self.loaded_json[self.show_name] = [x for x in self.loaded_json[self.show_name]].append(self.episode_file_name)
        print("holder: ", holder)

    def json_check_write_key(self):
        """
        This is check to see if a show exists in the JSON file, if it does, it will write a new key
        :return:
        """
        print("SHOW NAME", self.show_name)
        if self.show_name in self.loaded_json:
            print("SHOW IS FOUND ", str(self.show_name))
            return self, True
        else:
            self.loaded_json[str(self.show_name)] = self.episode_file_name
            return self, True

    def json_check_value(self):
        #we have to make sure that KEY (the show) exists first
        #Now we can see if the key has a value that matches the local file name. I
        obj_json = self.loaded_json
        if self.episode_file_name in obj_json[self.show_name]:
            print("EPISODE IS ALREADY IN JSON: ", str(self.episode_file_name), "is in : ", str(self.show_name))
            return True
        else:
            print("EPISODE IS NOT IN JSON: ", str(self.episode_file_name), "is not in : ", str(self.show_name))
            return False

    def json_update_value(self):
        print("RESULT UPDATE: ", str(result_update))
        if result_update is False:
            #The episode has not been downloaded and can downloaded and transferred
            #write the show to the list for the key
            holder_obj = self.loaded_json


            return self
        else:
            return self, False

    def json_write(self):
        result_update = self.json_update_value()
        if result_update is True:
            #Over Write Existsing JSON
            with open(self.json_file, 'w') as updated_file:
                #use
                json.dump()
            return True
        pass

    # WRITE NEW KEYS AND


test_json = JSONPodTracker(show_name='our_big_dumb_mouth', episode_file_name='OBDM660.mp3')
print("Loaded JSON 1: ", test_json.loaded_json)
test_json.json_check_write_key()
test_json.create_new_list_values()
print("Loaded JSON 2: ", test_json.loaded_json)
