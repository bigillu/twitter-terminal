import npyscreen
import curses
from twitterapi import client

# MAIN_WIDGET_CLASS   = wgmultiline.MultiLine
# MAIN_WIDGET_CLASS_START_LINE = 1
# STATUS_WIDGET_CLASS = wgtextbox.Textfield
# STATUS_WIDGET_X_OFFSET = 0
# COMMAND_WIDGET_CLASS= wgtextbox.Textfield
# COMMAND_WIDGET_NAME = None
# COMMAND_WIDGET_BEGIN_ENTRY_AT = None
# COMMAND_ALLOW_OVERRIDE_BEGIN_ENTRY_AT = True
# DATA_CONTROLER    = npysNPSFilteredData.NPSFilteredDataList
# ACTION_CONTROLLER  = ActionControllerSimple

MAX_TWEET_CHARS = 280

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

class TweetBox(npyscreen.MultiLineEdit):
    def exit_func(self, input):
        exit(0)

    def send_tweet(self, event):
        msg = self.value
        if msg is not "" and len(msg) <= MAX_TWEET_CHARS:
            client.send_tweet(msg)
            self.value = ""
            self.display()
        else:
            xcess_chars = len(msg) - MAX_TWEET_CHARS
            msg = "The tweet is {} characters more than the max limit".format(xcess_chars)

    def __init__(self, *args, **kargs):
        super(TweetBox,self).__init__(*args, **kargs)
        tweetbox_handlers = {
            "^D": self.exit_func,
            curses.ascii.alt(curses.ascii.NL): self.send_tweet
        }
        self.add_handlers(tweetbox_handlers)        


class TerminalForm(npyscreen.FormMutt):
        MAIN_WIDGET_CLASS = TimeLine
        MAIN_WIDGET_CLASS_START_LINE = 2
        COMMAND_WIDGET_CLASS = TweetBox

class TwitterTerminal(npyscreen.NPSApp):
    def main(self):
        F = TerminalForm()
        F.wStatus1.value = "Timeline"
        F.wStatus2.value = "Tweet"
        F.edit()


if __name__ == "__main__":
    App = TwitterTerminal()
    App.run()