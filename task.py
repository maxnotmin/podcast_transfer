#!/usr/bin/python3
import os
import sys
from celery import Celery

"""
This is the main file that will import all the other methods to be run as tasks
"""

app = Celery('task', broker='amqp://localhost/')

@app.task
def test_task(string=''):
    return string[::-1]