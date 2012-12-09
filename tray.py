#!/usr/bin/python

import appindicator, gtk, gobject, Gilly, time

class Example:
	def __init__(self):

		self.gilly = Gilly.GillyClass()

		self.ind = appindicator.Indicator("example","ball",appindicator.CATEGORY_APPLICATION_STATUS)
		self.ind.set_status(appindicator.STATUS_ACTIVE)
		self.ind.set_attention_icon("indicator-messages-new")
		#self.ind.set_label("Gilly")
		self.ind.set_icon("ball")

		self.menu = gtk.Menu()

		radio = gtk.RadioMenuItem(None,"India")
		radio.connect("toggled",self.callback,"India")
		radio.show()
		self.menu.append(radio)

		radio = gtk.RadioMenuItem(radio,"Australia")
		radio.connect("toggled",self.callback,"Aus")
		radio.show()
		self.menu.append(radio)

		radio = gtk.RadioMenuItem(radio,"West-Indies")
		radio.connect("toggled",self.callback,"West Indies")
		radio.show()
		self.menu.append(radio)

		item = gtk.MenuItem("Refresh")
		item.show()
		self.menu.append(item)

		check = gtk.CheckMenuItem("Auto-Refresh")
		check.show()
		self.menu.append(check)

		image = gtk.ImageMenuItem(gtk.STOCK_QUIT)
		image.connect("activate", self.quit)
		image.show()
		self.menu.append(image)

		self.menu.show()
		self.ind.set_menu(self.menu)

	def callback(self, widget, data=None):
		if widget.get_active():
			self.data = data
			if self.gilly.internet_on():
				self.gilly.parsing()
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
