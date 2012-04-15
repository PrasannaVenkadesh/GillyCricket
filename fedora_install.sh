#!/bin/bash

yum install tkinter python-feedparser
chmod +x Gilly.py Gillylive.py removeGilly.sh
cp Gilly.py Gillylive.py removeGilly.sh /opt/
ln -s /opt/Gilly.py /usr/bin/Gilly
ln -s /opt/Gillylive.py /usr/bin/Gillylive
ln -s /opt/removeGilly.sh /usr/bin/removeGilly
