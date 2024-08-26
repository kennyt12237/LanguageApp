from tkinter import Frame, Canvas, Scrollbar, Misc, Event
from tkinter import VERTICAL, RIGHT, ALL

from .GrammarFrame import GrammarFrame

from ..Window import Window
import json


class ScrollableGrammarFrame(Frame):

    GRAMMAR_FRAME = "gframe"

    def __init__(self, master: Misc, data: json = None, name='grammar', **kwargs) -> None:
        kwargs["name"] = name
        super().__init__(master, **kwargs)
        self.window: Window = self.winfo_toplevel()
        self.canvas = Canvas(self)
        self.scrollbar = Scrollbar(
            self, orient=VERTICAL, command=self.canvas.yview)
        self.grammarFrame = GrammarFrame(self.canvas, data)
        self.grammarFrame.grid_propagate(True)

        self.canvas.configure(
            yscrollcommand=self.scrollbar.set, yscrollincrement=75)
        self.canvas.create_window(
            (0, 0), anchor="nw", window=self.grammarFrame, tags=self.GRAMMAR_FRAME)

        self.canvas.bind("<Configure>", self.onCanvasConfigure)
        self.grammarFrame.bind("<Configure>", self.onFrameConfigure)

        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side=RIGHT, fill="y")
        self.pack_propagate(False)

    def onCanvasConfigure(self, event: Event) -> None:
        self.canvas.itemconfig(
            self.GRAMMAR_FRAME, width=self.canvas.winfo_width())

    def onFrameConfigure(self, event: Event) -> None:
        x, y, width, height = self.canvas.bbox(ALL)
        self.canvas.configure(scrollregion=(x, y, width, height - 75))
