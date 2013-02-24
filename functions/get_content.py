#!/usr/bin/python

class GUIValues():
    def __init__(self, window):
        # Fields in 'Basic' tab
        self.name = self.get_field(window, "entry_name")
        self.execute = self.get_field(window, "entry_exec")
        self.icon = self.get_field(window, "entry_icon")
        self.typeindex = self.get_type(window)
        self.category = self.get_combo(window, "cbox_category")
        self.useterm = self.get_switch(window, "switch_terminal")
        self.url = self.get_field(window, "entry_url")

        # Fields in 'Advanced' tab
        self.version = self.get_field(window, "entry_version")
        self.genericname = self.get_field(window, "entry_generic_name")
        self.nodisplay = self.get_switch(window, "switch_nodisplay")
        self.comment = self.get_field(window, "entry_comment")
        self.hidden = self.get_switch(window, "switch_hidden")
        self.notshowin = self.get_field(window, "entry_notshowin")
        self.tryexec = self.get_field(window, "entry_tryexec")
        self.path = self.get_field(window, "entry_path")
        self.mime = self.get_field(window, "entry_mime")
        self.keywords = self.get_field(window, "entry_keywords")
        self.notify = self.get_switch(window, "switch_notify")
        self.wmclass = self.get_field(window, "entry_wmclass")
        
        
    # Get the text of the fields
    def get_field(self, window, entry):
        return window.builder.get_object(entry).get_text()

    # Get the value of the switches
    def get_switch(self, window, switch):
        if window.builder.get_object(switch).get_active():
            return "true"
        else:
            return "false"

    # Get the value of the combo boxes
    def get_combo(self, window, combobox):
        model = window.builder.get_object(combobox).get_model()
        index = window.builder.get_object(combobox).get_active()
        return model[index][0]

    # Get the type of application to save
    def get_type(self, window):
        return window.builder.get_object("cbox_type").get_active()

