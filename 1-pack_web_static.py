#!/usr/bin/python3
'''
'''
from fabric.api import *
from time import strftime


def do_pack():
    '''
    '''
    now = strftime("%Y%m%d%H%M%S")
    try:
        local("sudo mkdir -p versions")
        local("sudo tar -cvzf versions/web_static_{}.tgz web_static".format(
            now))
    except:
        return None
    return "versions/web_static_{}.tgz".format(now)
