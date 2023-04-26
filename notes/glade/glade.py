#!/usr/bin/env python3

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class WindowMain(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self)
        self.button = Gtk.Button(label="Click Here")
        self.button.connect("clicked", self.on_button1_clicked)
        self.add(self.button)

    def on_button1_clicked(self, widget):
        print("Hello World")

    def main(self):
        Gtk.main()


if __name__ == "__main__":
    application = WindowMain()
    application.main()
