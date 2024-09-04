from tkinter import Misc, Label, Button
from tkinter import E

from .SentenceFrame import SentenceFrame
from ....Section import GridFrame


class SettingFrame(GridFrame):

    CLOSE = "Close"
    HEADER = "Setting"

    def __init__(self, master: Misc, **kwargs) -> None:
        super().__init__(master, **kwargs)
        self.header = Label(self, text=self.HEADER)
        self.sentenceSettingFrame = SentenceFrame(self)
        self.closeButton = Button(self, text=self.CLOSE)
        self._gridPlacement()

    def setOnClosedButtonPressed(self, command) -> None:
        self.closeButton.config(command=command)

    def _gridPlacement(self) -> None:
        self.header.grid(row=0, column=0)
        self.sentenceSettingFrame.grid(row=1, column=0, pady=(0, 50))
        self.closeButton.grid(row=2, column=0, sticky=E)
        self.grid_columnconfigure(0, weight=1)
