#!/usr/bin/env python 
"""
Application Name:- Gilly
Version:- 1.0
Author:- Prasanna Venkadesh (http://prasopensource.wordpress.com)
License:- GNU GPL V3.0
CopyLeft April, 2012 Prasanna Venkadesh

"""
from Tkinter import *
import feedparser
import pynotify

def parsing():
	T.delete(1.0,END)
	source=['http://static.cricinfo.com/rss/livescores.xml']
	file = open("feeds", "w+")
	for url in source:
	    data = feedparser.parse(url)
	    for entry in data.entries:
		file.write(entry.title + "\n\n")
	file.close()
	
	pynotify.init("Gilly Cricket")
	notification = pynotify.Notification ("Success!", "Score fetched.", "dialog-information")
	notification.show()

	file_read = open("feeds","r+")
	content = file_read.read()
	T.insert(INSERT, content)
	file_read.close()


root = Tk()
root.title("Gilly V-1.0")

content =StringVar()
T=Text(root,height=10,width=60)
T.pack()
B=Button(root, text="Update", command=parsing)
B.pack()

root.mainloop()
