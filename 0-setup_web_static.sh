#!/usr/bin/env bash
# a Bash script that sets up your web servers for the deployment of web_static
sudo apt-get -y update
sudo apt-get -y install nginx
sudo mkdir -p /data/
sudo mkdir -p /data/web_static/
sudo mkdir -p /data/web_static/releases/
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
echo -e "testing..." | sudo tee /data/web_static/releases/test/index.html
sudo ln -s /data/web_static/releases/test/ /data/web_static/current
sudo chown -hR ubuntu:ubuntu /data/
sudo sed -i "s/http {/http {add_header X-Served-By \$HOSTNAME;/" /etc/nginx/nginx.conf
sudo sed -i "s/server_name _;/server_name _;\n\tlocation \/hbnb_static {\n\t\talias\/data\/web_static\/current\/;\n\t}/" /etc/nginx/sites-available/default
sudo service nginx restart
