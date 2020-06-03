import npyscreen
from src.mainform import MainForm


class TwitterTerminal(npyscreen.StandardApp):

    def onStart(self):
        self.MainForm = self.addForm("MAIN", MainForm)
