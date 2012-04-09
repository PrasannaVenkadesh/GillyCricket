#!/usr/bin/env python 
"""
Application Name:- Gilly
Version:- 1.0
Authors:- Prasanna Venkadesh (http://prasopensource.wordpress.com)
	 Ganesh Katrapati (neshmailsu@gmail.com)
License:- GNU GPL V3.0
CopyLeft April, 2012 Prasanna Venkadesh

"""
from Tkinter import *
import feedparser
import pynotify
import threading 
import time 
import sys

minutes = sys.argv[1]

#Thread for running Gilly every 30 seconds

class Gilly (threading.Thread):
	def run (self):
		while True:
			self.parsing()
			time.sleep(60*int(minutes))
	def parsing(self):

		source=['http://static.cricinfo.com/rss/livescores.xml']
		text = ""
		pynotify.init("Gilly Cricket")
		for url in source:
		    data = feedparser.parse(url)
		    for entry in data.entries:
    			notification = pynotify.Notification (entry.title, "Score fetched.", "dialog-information")
			notification.show()

pynotify.init("Gilly Cricket")
notification = pynotify.Notification ("Gilly Cricket Active!", "Score will be fetched every "+minutes+" minutes", "dialog-information")
notification.show()
Gilly().start()
