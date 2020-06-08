import npyscreen
from src.twitterapi import client


class TimeLine(npyscreen.MultiLineEdit):
    def exit_func(self, input):
        exit(0)

    def display_timeline(self,event):
        tl = client.get_timeline()
        self.value = "\n".join(tl) 

    def __init__(self, *args, **kargs):
        super(TimeLine,self).__init__(*args, **kargs)
        timeline_handlers = {
            "^D": self.exit_func,
            "^N": self.display_timeline
        }
        self.editable = 'false'
        self.add_handlers(timeline_handlers)        