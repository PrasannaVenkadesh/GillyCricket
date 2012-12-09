#!/usr/bin/env python 
"""
Application Name:- Gilly
Version:- 1.0
Author:- Prasanna Venkadesh (http://prasopensource.wordpress.com)
License:- GNU GPL V3.0
CopyLeft April, 2012 Prasanna Venkadesh

"""

import pynotify, os, urllib2, re

class GillyClass:
	def __init__(self):
		pynotify.init("Gilly Cricket")

	def country(self,name):
		self.flag = True
		read_again = open("feeds","r+")
		lines = read_again.readlines()
		for i in lines:
			if re.search(name,i):
				#print i
				notification = pynotify.Notification (i.title(), "Latest Update", "stumps")
				notification.show()
				self.flag = False
		if self.flag:
			print "no match"
			notification = pynotify.Notification("No Current Match", "Check later", "cry")
			notification.show()
			self.flag = False
		#print line[0]
		read_again.close()

	def internet_on(self):
		try:
			response = urllib2.urlopen('http://www.google.com', timeout=3)
			return True
		except urllib2.URLError:
			return False
