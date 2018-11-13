# podcast_transfer
This script will reach out to target podcast RSS feeds, get the newest episode and transfer that mp3 to a target server

## STEPS
*technologies used: Python3, [Apache Airflow](https://airflow.apache.org/)

Airflow Server (the scheduler)
_apache airflow will run on a schedule that will run every day at 1am to run the main.py file to perform the following operations_

**Tech Install Cards** on [Digital Ocean](https://www.digitalocean.com/) Droplets
+ Determine if: Apache Airflow or Celery is the correct scheduler for this project. | _points_: **8** |
+ Install and Configure Apache Airflow (Used to schedule and execute python code).  | _points_: **20** |  _this is new technology and I must determine the best way install and replicate installation. Examine use of Docker_
+ + Determine is RabbitMQ will be required for current or future scheduling | _points_: **8** |
+ Install and Configure Celery (Used to schedule and execute python code).  | _points_: **13** 
+ Install MySQL or PostgreSQL (Used to log file transfers) | _points_: **13** |

**Programming Story Cards**
1. Load INI File (INI file contains all URL to target RSS Feeds) and create in memory list()
    - **Cards**:
    - Create Configparser method that returns a list[str] of RSS URL from INI file | **Card**: points: **5**
    - Create Configparser method the returns a dict[str:str] of FTP information | **Card**: points: **5**

2. Fetch Most Recent Podcast Episode from RSS URL supplied by Config INI
    - **Cards**:
    - Create FeedParser Class that will be created for each podcast RSS Feed. | **Card**: points: **5**
    - 
    
3. Transfer File to Target Sever
    - **Cards**:

4. Write File Transfer Information to Database
    - **Cards**:

5. Notification of status of file transfer
    - **Cards**: