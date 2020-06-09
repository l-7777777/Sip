import xml.etree.ElementTree as ET
import json
import tkinter as tk

configfile = open("config.json", "r")
config = json.loads(configfile.read())

tree = ET.parse(config["path"])
XMLroot = tree.getroot()

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        for child in XMLroot:
            exec("self." + child.attrib["name"] + " = tk." + child.tag + "(self)")
            exec("self." + child.attrib["name"] + "['text'] = '" + child.text + "'")
            exec("self." + child.attrib["name"] + ".pack(side='top')")
            for attribute in child.attrib:
                if attribute != "name":
                    exec("self." + child.attrib["name"] + "['" + attribute + "']" + " = '" + child.attrib[attribute] + "'")

root = tk.Tk()
app = Application(master=root)
app.mainloop()