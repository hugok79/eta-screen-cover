#!/usr/bin/python3

import os
import sys
import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gio, Gtk

from MainWindow import MainWindow


class Application(Gtk.Application):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, application_id="tr.org.eta.ekran-karartma", **kwargs)
        self.window = None

    def do_activate(self):
        self.window = MainWindow(self)
        self.window.show_ui()


app = Application()
app.run(sys.argv)
