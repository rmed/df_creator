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

    def newFile(self, widget):
        entries = {
            "entry_name", "entry_command", "entry_icon", "entry_type"
        }
        #self.builder.get_object("entry_name").set_text('')
        for entry in entries:
            self.builder.get_object(entry).set_text('')
        

    def saveFile(self, widget):
        print "Yet to implement"
        
window = MainGui()
Gtk.main()


