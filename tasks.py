#!/usr/bin/python3
import os
import sys
from celery import Celery
from celery_db import *

"""
This is the main file that will import all the other methods to be run as tasks
"""
cel_db_path = ab_path_dir_file_db

app = Celery('task', broker='amqp://localhost/')

@app.task
def test_task(string=''):
    print("FROM TEST TASK: ", str(cel_db_path))
    return 'MESSAGE: {the_string} | {db_path}'.format(the_string=string, db_path=cel_db_path)