__author__ = 'Trevor'

import sqlite3
import feedparser
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from ReadRss import DatabaseOperations

class Widgets(GridLayout):
    def __init__(self):
        print "Hi"
    def testmethod(self):
        layout = GridLayout(cols=1, spacing=10, size_hint_y=None)
        #Make sure the height is such that there is something to scroll.
        layout.bind(minimum_height=layout.setter('height'))
        x = DatabaseOperations()
        for i in x.getAll():
            btn = Label(text=i.encode('utf-8'), size_hint_y=None, size=(self.width, self.height),
                        text_size=(self.width+50, self.height+50), valign='middle', halign='right')
            layout.add_widget(btn)
        root = ScrollView(size_hint=(None, None), size=(400, 400), pos_hint={'center_x':.5, 'center_y':.5})
        root.add_widget(layout)
        return root

class Kivyexample(App):
    def build(self):
        t = Widgets()
        return t.testmethod()

if __name__ == "__main__":
    Kivyexample().run()