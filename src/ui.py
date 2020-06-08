import npyscreen
from src.mainform import MainForm


class TwitterTerminal(npyscreen.NPSApp):
    def main(self):
        F = MainForm()
        F.wStatus1.value = "Timeline"
        F.wStatus2.value = "Tweet"
        F.edit()