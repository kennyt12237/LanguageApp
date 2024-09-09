from tkinter import Label
from tkinter import HORIZONTAL, W
from tkinter.ttk import Separator

from .ToggleFrame import ToggleFrame
from ....Section import Window, GridFrame
from ....Section import dictionaryWordTooltipDefault, grammarTooltipDefault

from abc import ABC, abstractmethod

class SymbolLabelToggle(ABC, GridFrame):
    
    def __init__(self, master, text : str, **kwargs) -> None:
        super().__init__(master, **kwargs)
        self.headerLabel = Label(
            self, text=text, width=40, padx=4, anchor=W)
        self.seperator2 = Separator(self, orient=HORIZONTAL)
        self.toogleFrame = ToggleFrame(self)
        self.toogleFrame.setOffRadioButtonPressed(
            lambda: self.onToogleOffPressed())
        self.toogleFrame.setOnRadioButtonPressed(
            lambda: self.onToogleOnPressed())
        self._gridPlacement()
        
    @abstractmethod
    def onToogleOffPressed(self) -> None:
        pass
    
    @abstractmethod
    def onToogleOnPressed(self) -> None:
        pass

    def _gridPlacement(self) -> None:
        self.headerLabel.grid(row=0, column=0, sticky="nsew")
        self.seperator2.grid(row=1, column=0, sticky="ew", pady=(0, 2))
        self.toogleFrame.grid(row=2, column=0, sticky="nsew")
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_columnconfigure(0, weight=1)
        
class DictionaryTooltipToggle(SymbolLabelToggle):
    
    def __init__(self, master, **kwargs) -> None:
        super().__init__(master, text="Dictionary Tooltip", **kwargs)
    
    def onToogleOffPressed(self) -> None:
        window: Window = self.winfo_toplevel()
        window.addWidgetStyling("wordLabel", dict(
            background=window.cget("background")))
        window.addWidgetStyling("wltooltip", dict(state="disabled"))

    def onToogleOnPressed(self) -> None:
        window: Window = self.winfo_toplevel()
        window.addWidgetStyling("wordLabel", dictionaryWordTooltipDefault)
        window.addWidgetStyling("wltooltip", dict(state="normal"))
        
class GrammarTooltipToggle(SymbolLabelToggle):
    
    def __init__(self, master, **kwargs) -> None:
        super().__init__(master, text="Grammar Tooltip", **kwargs)
    
    def onToogleOffPressed(self) -> None:
        window: Window = self.winfo_toplevel()
        window.addWidgetStyling("grammarLabel", dict(
            background=window.cget("background")))
        window.addWidgetStyling("gltooltip", dict(state="disabled"))

    def onToogleOnPressed(self) -> None:
        window: Window = self.winfo_toplevel()
        window.addWidgetStyling("grammarLabel", grammarTooltipDefault)
        window.addWidgetStyling("gltooltip", dict(state="normal"))