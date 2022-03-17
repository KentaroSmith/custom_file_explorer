from kivy.lang.builder import Builder
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.app import App
import kivy
import pathlib
kivy.require('2.1.0')

Builder.load_file("explorer.kv")


class Folder(Widget):
    def build():
        drive = pathlib.Path.home().drive
        return Label(text=drive)


class FolderApp(App):
    def build(self):
        Folder.build()
        return Folder()


if __name__ == '__main__':
    FolderApp().run()
