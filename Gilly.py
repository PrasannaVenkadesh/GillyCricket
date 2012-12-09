#!/usr/bin/env python 
"""
Application Name:- Gilly
Version:- 1.0
Author:- Prasanna Venkadesh (http://prasopensource.wordpress.com)
License:- GNU GPL V3.0
CopyLeft April, 2012 Prasanna Venkadesh

"""

import feedparser, re
import pynotify, os, urllib2

class GillyClass:
	def __init__(self):
		self.flag = True
	
	def parsing(self):
		source=['http://static.cricinfo.com/rss/livescores.xml']
		file = open("feeds", "w+")
		for url in source:
			data = feedparser.parse(url)
	    	for entry in data.entries:
			file.write(entry.title + "\n\n")
		file.close()
	
		pynotify.init("Gilly Cricket")
		


	def country(self,name):
		read_again = open("feeds","r+")
		lines = read_again.readlines()
		for i in lines:
			if re.search(name,i):
				#print i
				notification = pynotify.Notification (i, "Current Score", "crickfinal")
				notification.show()
				self.flag = False
		if self.flag:
			notification = pynotify.Notification("No Current Match", "Check later", "sad")
			notification.show()
		#print line[0]
		read_again.close()
		os.remove("feeds")

	def internet_on(self):
		try:
			response = urllib2.urlopen('http://www.google.com', timeout=3)
			return True
		except urllib2.URLError:
			return False