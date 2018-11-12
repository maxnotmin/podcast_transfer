# podcast_transfer
This script will reach out to target podcast RSS feeds, get the newest episode and transfer that mp3 to a target server

## STEPS
*technologies used: Python3, [Apache Airflow](https://airflow.apache.org/)

Location : Airflow Server (The Brain)
_apache airflow will run on a schedule that will run every day at 1am to run the main.py file to perform the following operations_
1. Load INI File (INI file contains all URL to target RSS Feeds) and create in memory list()
    Cards:
        * Create Configparser method that returns a list[str] of RSS URL from INI file : points: 5

2.
