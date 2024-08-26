from tkinter import Frame, Canvas, Scrollbar, Misc, Event
from tkinter import VERTICAL, RIGHT, ALL

from .DictionaryFrame import DictionaryFrame

from ....Window import Window
import json


class ScrollableDictionaryFrame(Frame):

    def __init__(self, master: Misc, data: json = None, **kwargs) -> None:
        super().__init__(master, **kwargs)
        self.window: Window = self.winfo_toplevel()
        self.canvas = Canvas(self)
        self.scrollbar = Scrollbar(
            self, orient=VERTICAL, command=self.canvas.yview)
        self.dictionaryFrame = DictionaryFrame(self.canvas, data)
        self.dictionaryFrame.grid_propagate(True)

        self.canvas.configure(
            yscrollcommand=self.scrollbar.set, yscrollincrement=150)
        self.canvas.create_window(
            (0, 0), anchor="nw", window=self.dictionaryFrame, tags="frame")

        self.canvas.bind("<Configure>", self.onCanvasConfigure)
        self.dictionaryFrame.bind("<Configure>", self.onFrameConfigure)

        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side=RIGHT, fill="y")
        self.pack_propagate(False)

    def onCanvasConfigure(self, event: Event) -> None:
        self.canvas.itemconfig("frame", width=self.canvas.winfo_width())

    def onFrameConfigure(self, event: Event) -> None:
        x, y, width, height = self.canvas.bbox(ALL)
        canvasHeight = self.canvas.winfo_height()
        bottomRegion = height - canvasHeight
        
        if event.y >= 0:
            self.canvas.yview_moveto(0.0)
        elif event.y <= -bottomRegion:
            self.canvas.yview_moveto(bottomRegion/height)
            
        self.canvas.configure(scrollregion=(x, y, width, height))
