import npyscreen
import curses
from src.twitterapi import client


MAX_TWEET_CHARS = 280

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