#!/usr/bin/python

"""
Application Name:- Gilly Cricket
Version:- 1.0
Author:- Prasanna Venkadesh (http://prasopensource.wordpress.com)
License:- GNU GPL V3.0
CopyLeft April, 2012 Prasanna Venkadesh

"""

import appindicator, gtk, gobject, Gilly, time
from threading import Timer

class Example:
	def __init__(self):

		self.gilly = Gilly.GillyClass()

		self.ind = appindicator.Indicator("example","ball",appindicator.CATEGORY_APPLICATION_STATUS)
		self.ind.set_status(appindicator.STATUS_ACTIVE)
		self.ind.set_attention_icon("indicator-messages-new")
		#self.ind.set_label("Gilly")
		self.ind.set_icon("ball")

		self.menu = gtk.Menu()

		listMenu = gtk.Menu()

		listItems = gtk.MenuItem("Country")
		listItems.set_submenu(listMenu)

		self.menu.append(listItems)

		radio = gtk.RadioMenuItem(None,"India")
		radio.connect("toggled",self.callback,"india")
		radio.show()
		listMenu.append(radio)

		radio = gtk.RadioMenuItem(radio,"Australia")
		radio.connect("toggled",self.callback,"aus|perth")
		radio.show()
		listMenu.append(radio)

		radio = gtk.RadioMenuItem(radio,"West-Indies")
		radio.connect("toggled",self.callback,"west indies")
		radio.show()
		listMenu.append(radio)

		radio = gtk.RadioMenuItem(radio,"England")
		radio.connect("toggled",self.callback,"england")
		radio.show()
		listMenu.append(radio)

		radio = gtk.RadioMenuItem(radio,"Sri-Lanka")
		radio.connect("toggled",self.callback,"sri lanka")
		radio.show()
		listMenu.append(radio)

		radio = gtk.RadioMenuItem(radio,"Bangladesh")
		radio.connect("toggled",self.callback,"bangladesh|bangla")
		radio.show()
		listMenu.append(radio)

		radio = gtk.RadioMenuItem(radio,"NewZealand")
		radio.connect("toggled",self.callback,"nz|new-zealand")
		radio.show()
		listMenu.append(radio)


		image = gtk.ImageMenuItem(gtk.STOCK_QUIT)
		image.connect("activate", self.quit)
		image.show()
		self.menu.append(image)

		listMenu.show()
		listItems.show()
		self.menu.show()
		self.ind.set_menu(self.menu)
		

	def callback(self, widget, data=None):
		if widget.get_active():
			self.data = data
			if self.gilly.internet_on():
				self.gilly.country(self.data)
			else:
				message = gtk.MessageDialog(type=gtk.MESSAGE_ERROR, buttons=gtk.BUTTONS_NONE)
				message.set_markup("Check your Internet Connection !")
				message.run()

	def quit(self, widget, data=None):
		gtk.main_quit()

def main():
	gtk.main()
	return 0

if __name__ == '__main__':
	ex = Example()
	main()
