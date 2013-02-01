from gi.repository import Gtk

class MainGui:
    
    def __init__(self):
        self.builder = Gtk.Builder()
        self.builder.add_from_file("gui/main.glade")
        self.builder.connect_signals(self)
        self.win = self.builder.get_object("window1")
        self.win.show_all()

    def onDeleteWindow(self, *args):
        Gtk.main_quit(*args)

    def onChooseIcon(self, widget):
        print "Hello World"
        
window = MainGui()
Gtk.main()


