#!/usr/bin/env bash

sudo rm -rf /etc/nginx/sites-enabled/*
sudo ln -s $HOME/PythonWeb/git_notification/setup/nginx_notifications.conf /etc/nginx/sites-enabled/nginx_notifications.conf