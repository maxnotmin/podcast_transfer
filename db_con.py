import sys
import os
import sqlite3


AB_PATH = os.path.abspath(__file__)
CUR_DIR = os.getcwd()

DB_DIR = 'db'
DB_FILE = 'celery_db.sqlite'

ab_path_dir_db = os.path.join(AB_PATH, DB_DIR)

ab_path_dir_file_db = os.path.join(ab_path_dir_db, DB_FILE)


def db_test_con():
    pass