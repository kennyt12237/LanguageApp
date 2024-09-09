from tkinter import Label
from tkinter import HORIZONTAL, W
from tkinter.ttk import Separator


from .ToggleFrame import ToggleFrame
from ....Section import Window, GridFrame
from ....Section import dictionaryWordTooltipDefault

class DictionaryWordToggle(GridFrame):
    
    def __init__(self, master, **kwargs) -> None:
        super().__init__(master, **kwargs)
        self.dictionaryTooltipLabel = Label(
            self, text="Dictionary Tooltip", width=40, padx=4, anchor=W)
        self.seperator2 = Separator(self, orient=HORIZONTAL)
        self.toogleFrame = ToggleFrame(self)
        self.toogleFrame.setOffRadioButtonPressed(
            lambda: self.onToogleOffPressed())
        self.toogleFrame.setOnRadioButtonPressed(
            lambda: self.onToogleOnPressed())
        self._gridPlacement()
        
    def onToogleOffPressed(self) -> None:
        window: Window = self.winfo_toplevel()
        window.addWidgetStyling("wordLabel", dict(
            background=window.cget("background")))
        window.addWidgetStyling("wltooltip", dict(state="disabled"))

    def onToogleOnPressed(self) -> None:
        window: Window = self.winfo_toplevel()
        window.addWidgetStyling("wordLabel", dictionaryWordTooltipDefault)
        window.addWidgetStyling("wltooltip", dict(state="normal"))

    def _gridPlacement(self) -> None:
        self.dictionaryTooltipLabel.grid(row=0, column=0, sticky="nsew")
        self.seperator2.grid(row=1, column=0, sticky="ew", pady=(0, 2))
        self.toogleFrame.grid(row=2, column=0, sticky="nsew")
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_columnconfigure(0, weight=1)