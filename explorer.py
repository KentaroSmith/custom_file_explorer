from kivy.lang.builder import Builder
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.app import App
import kivy
import os
import pathlib

kivy.require('2.1.0')

root_widget = Builder.load_file("explorer.kv")
current_directory = pathlib.Path.home().drive


class address_bar(Widget):
    pass


class directory(Widget):
    pass


class Folder(Widget):
    def make_address_bar():
        address_bar = TextInput(text=current_directory, multiline=False)
        return address_bar

    def list_files(this_directory):
        directory_contents = os.listdir(this_directory)
        return directory_contents

    def build():
        pass


class FolderApp(App):
    def change_directory(self, new_location):
        os.chdir(new_location)
        current_directory = pathlib.Path.cwd

    def build(self):
        self.title = "File Explorer"
        b = BoxLayout(orientation='vertical')
        address_bar = TextInput(
            font_size=15,
            size_hint_y=None,
            height=30,
            multiline=False,
            text=current_directory,
            pos_hint={'top': 1}
        )
        submit = Button(text='Submit')
        submit.bind(on_press=lambda x: self.change_directory(address_bar.text))
        b.add_widget(address_bar)
        b.add_widget(submit)
        f = FloatLayout()
        Folder.build()
        directory_items = os.listdir(current_directory)
        for item in directory_items:
            label = Label(text=item, font_size='15', color='7f7f7f')
            b.add_widget(label)
        return b


if __name__ == '__main__':
    FolderApp().run()
