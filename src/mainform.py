import npyscreen
import curses
from src.tweetbox import TweetBox
from src.timeline import TimeLine


class MainForm(npyscreen.FormMutt):
        MAIN_WIDGET_CLASS = TimeLine
        MAIN_WIDGET_CLASS_START_LINE = 2
        COMMAND_WIDGET_CLASS = TweetBox
