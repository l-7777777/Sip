import xml.etree.ElementTree as ET
import json
import mysql.connector
import tkinter as tk
import os

configfile = open("config.json", "r")
config = json.loads(configfile.read())

tree = ET.parse(config["path"])
XMLInfo = tree.find("info")
XMLView = tree.find("view")
XMLLogic = tree.find("logic")
XMLRoot = tree.getroot()


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        for child in XMLView:
            if child.tag == "echo":
                for baby in child:
                    if baby.tag == "python":
                        exec(
                            "self." + baby.attrib["name"] + " = tk.Label(self)")
                        exec(
                            "self." + baby.attrib["name"] + '["text"] = "' + str(eval(baby.text)) + '"')
                        exec(
                            "self." + baby.attrib["name"] + ".pack(side='" + baby.attrib["side"] + "')")
            else:
                exec("self." + child.attrib["name"] +
                     " = tk." + child.tag + "(self)")
                exec("self." + child.attrib["name"] +
                     "['text'] = '" + child.text + "'")
                exec("self." + child.attrib["name"] +
                     ".pack(side='" + child.attrib["side"] + "')")
                for attribute in child.attrib:
                    if attribute != "name" and attribute != "side":
                        exec("self." + child.attrib["name"] + "['" + attribute +
                             "']" + " = '" + child.attrib[attribute] + "'")


for child in XMLLogic:
    if child.tag == "database":
        exec(child.attrib["name"] + " = mysql.connector.connect(host = '" + child.attrib["host"] + "', user = '" + child.attrib["user"] + "', password = '" + child.attrib["password"] + "')")
        for command in child:
            exec(child.attrib["name"] + ".cursor().execute('" + command.text + "')")

root = tk.Tk()
root.title(XMLInfo.find("title").text)
if XMLRoot.attrib["width"]:
    root.geometry(XMLRoot.attrib["width"] + "x" + XMLRoot.attrib["height"])
app = Application(master=root)
app.mainloop()