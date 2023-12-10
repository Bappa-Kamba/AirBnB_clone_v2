#!/usr/bin/env bash
# Bash script that sets up web servers for the deployment of web_static

if ! dpkg -l | grep -q "nginx"; then
	sudo apt-get update && sudo apt-get install -y nginx
fi
sudo mkdir -p /data/web_static/{releases/test,shared}

echo "This is a test file." | sudo tee /data/web_static/releases/test/index.html > /dev/null

if [ -L /data/web_static/current ]; then
	sudo rm /data/web_static/current	
fi
sudo ln -sf /data/web_static/releases/test /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
echo "server {
    listen 80 default_server;
    listen [::]:80 default_server;

    #root /data/;

    index index.html index.htm index.nginx-debian.html;

    server_name _;

    location /hbnb_static {
        alias /data/web_static/current/;
        index index.html;
    }
}" | sudo tee /etc/nginx/sites-available/default > /dev/null

# Restart Nginx
sudo service nginx restart
echo "Server reloaded"
