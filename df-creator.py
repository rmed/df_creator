from gi.repository import Gtk

class MainGui:
    
    def __init__(self):
        self.builder = Gtk.Builder()
        self.builder.add_from_file("gui/df-creator.glade")
        self.builder.connect_signals(self)
        self.win = self.builder.get_object("main_window")
        self.win.show_all()

    def on_delete_window(self, *args):
        Gtk.main_quit(*args)

    def on_new_click(self, widget):
        entries = {
            "entry_name", "entry_command", "entry_icon", "entry_type"
        }
        for entry in entries:
            self.builder.get_object(entry).set_text('')

        self.builder.get_object("switch_terminal").set_active(False)
        
    def on_save_click(self, widget):
        print "Yet to implement"
        
        
window = MainGui()
Gtk.main()


