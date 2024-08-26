from tkinter import Button, Misc
from tkinter import CENTER
from typing import Callable

from .SectionFrame import ScrollableDictionaryFrame, SectionFrame, GridFrame, Window, convertPixelsToTextUnit


class HomeFrame(GridFrame):

    def __init__(self, master: Misc, defaultWidgetSize: float = 0.1, **kwargs):
        super().__init__(master, **kwargs)
        self.window: Window = self.winfo_toplevel()
        self.defaultWidgetSize = defaultWidgetSize
        self.getDictionaryData: Callable = None
        self.getSectionsData: Callable = None
        self.dictionaryButton = Button(
            self, text="Dictionary", command=self.onDictionaryButtonPressed)
        self.sectionButton = Button(
            self, text="Sections", command=self.onSectionsButtonPressed)
        self.setAllButtonSizeRelativeToScreen(defaultWidgetSize)
        self._gridPlacement()

    def setAllButtonSizeRelativeToScreen(self, relativeSize: float) -> None:
        widthPixel = int(self.window.getWidth() * relativeSize)
        heightPixel = int(self.window.getHeight() * relativeSize)
        for child in self.winfo_children():
            if isinstance(child, Button):
                width, height = convertPixelsToTextUnit(
                    child, widthPixel, heightPixel)
                child.config(width=width, height=height)

    def setGetDictionaryData(self, method: Callable) -> None:
        self.getDictionaryData = method

    def onDictionaryButtonPressed(self) -> None:
        self.window.newFrameNavigated(ScrollableDictionaryFrame(
            self.window, self.getDictionaryData(), name="dictionary"))

    def setGetSectionsData(self, method: Callable) -> None:
        self.getSectionsData = method

    def onSectionsButtonPressed(self) -> None:
        self.window.newFrameNavigated(SectionFrame(
            self.window, self.getSectionsData(), name="section"))

    def _gridPlacement(self) -> None:
        self.dictionaryButton.grid(row=0, column=0, pady=(0, 20))
        self.sectionButton.grid(row=1, column=0)

    def _setGridProperties(self) -> None:
        self.grid_propagate(False)
        self.grid_anchor(CENTER)
