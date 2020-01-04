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
        local("mkdir -p /versions")
        local("tar -cvzf /versions/web_static{}.tgz web_static".format(now))
    except:
        return None
    return "/versions/web_static_{}.tgz".format(now)
