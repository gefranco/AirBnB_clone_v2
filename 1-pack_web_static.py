#!/usr/bin/python3
'''
'''
from fabric.api import *
import datetime

env.hosts = [
    '35.227.43.49',
]
env.user = "ubuntu"
env.key_filename = './holberton'


def do_pack():
        '''
        '''
        now = datetime.datetime.now()
        get_status = get(remote_path="/data/web_static/",
            local_path="/versions/web_static_{}{}{}{}{}{}.tgz".format
            (now.year, now.month, now.day, now.hour, now.minute, now.second))
        return get_status
