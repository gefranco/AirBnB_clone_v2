#!/usr/bin/python3
'''
'''
from fabric.api import *
from time import strftime
from os import path

env.hosts = [
    '35.227.43.49',
    '35.231.164.230'
]
#env.user = "ubuntu"
#env.key_filename = './holberton'


def do_pack():
    '''
    '''
    now = strftime("%Y%m%d%H%M%S")
    try:
        local("sudo mkdir -p versions")
        local("sudo tar -cvzf versions/web_static{}.tgz web_static".format(
            now))
    except:
        return None
    return "versions/web_static_{}.tgz".format(now)


def do_deploy(archive_path):
    '''
    '''
    if not path.exists(archive_path):
        print("no file")
        return False

    try:
        name_archive = archive_path.split("/")[1]
        name_alone = name_archive.split(".")[0]
        put(archive_path, "/tmp/")
        sudo("mkdir -p /data/web_static/releases/{}".format(name_alone))
        sudo("tar -xvzf /tmp/{} -C /data/web_static/releases/{}".format(name_archive, name_alone))
        sudo("rm /tmp/{}".format(name_archive))
        sudo("mv /data/web_static/releases/{}/web_static/* /data/web_static/releases/{}".format(name_alone, name_alone))
        sudo("rm -rf /data/web_static/releases/{}/web_static".format(name_alone))
        sudo("unlink /data/web_static/current")
        sudo("ln -s /data/web_static/releases/{} /data/web_static/current".format(name_alone))
        return True
    except:
        return False
