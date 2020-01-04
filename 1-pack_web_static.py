#!/usr/bin/python3
'''
'''
from fabric.api import *
from time import strftime

env.hosts = [
    '35.227.43.49',
]
env.user = "ubuntu"
env.key_filename = './holberton'


def do_pack():
    '''
    '''
    now = strftime("%Y%m%d%H%M%S")
    try:
        get(remote_path="/data/web_static/",
            local_path="/versions/web_static_{}.tgz".format
            (now))
    except:
        return None
    return "/versions/web_static_{}.tgz".format(now)
