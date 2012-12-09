#!/usr/bin/python
"""
Application Name:- Gilly
Version:- 1.0
Author:- Prasanna Venkadesh (http://prasopensource.wordpress.com)
License:- GNU GPL V3.0
CopyLeft April, 2012 Prasanna Venkadesh

"""

import time, feedparser


def parsing():
	source=['http://static.cricinfo.com/rss/livescores.xml']
	file = open("feeds", "w+")
	for url in source:
		data = feedparser.parse(url)
	   	for entry in data.entries:
			file.write(entry.title.lower() + "\n\n")
	file.close()

	
while True:
	parsing()
	time.sleep(60)
