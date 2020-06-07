import npyscreen
import curses
from src.tweetbox import TweetBox
from src.timeline import TimeLine
from src.twitterapi import client

MAX_TWEET_CHARS = 280

class MainForm(npyscreen.FormBaseNew):
    def create(self):
        # Window Size
        y, x = self.useable_space()
        # Setup widgets
        self.tweetBox = self.add(TweetBox, name='Tweet?',rely=-7, editable='true')
        self.timeLine = self.add(TimeLine, name="Timeline", editable='false',custom_highlighting=True, 
              rely=y // 8 -3, max_height=y // -12)

        new_handlers = {
            "^D": self.exit_func,
            curses.ascii.alt(curses.ascii.NL): self.send_tweet
        }
        self.add_handlers(new_handlers)

    # def while_waiting(self):
        # tl = client.get_timeline()
        # self.timeLine.value = "\n".join(tl)
        # print("\n".join(tl))
        
    def send_tweet(self, event):
        msg = self.tweetBox.value
        if msg is not "" and len(msg) <= MAX_TWEET_CHARS:
            client.send_tweet(msg)
            self.tweetBox.value = ""
            self.tweetBox.display()
        else:
            xcess_chars = len(msg) - MAX_TWEET_CHARS
            msg = "The tweet is {} characters more than the max limit".format(xcess_chars)

    def exit_func(self, _input):
        exit(0)

