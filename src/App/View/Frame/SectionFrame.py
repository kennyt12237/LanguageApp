from tkinter import Button, Misc
from tkinter import CENTER
import json

from ..Window import Window
from ..Utils import convertPixelsToTextUnit
from .SectionContentFrame import SectionContentFrame
from .AbstractFrame import GridFrame


class SectionFrame(GridFrame):

    def __init__(self, master: Misc, data: json = None, defaultWidgetSize: float = 0.1, **kwargs) -> None:
        super().__init__(master, **kwargs)
        self.window: Window = self.winfo_toplevel()
        self.sections = json.loads(data)
        self._createButtons()
        self.setAllButtonSizeRelativeToScreen(defaultWidgetSize)
        self._gridPlacement()

    def _createButtons(self) -> None:
        def createSectionContentFrame(text, sectionData) -> None:
            self.window.newFrameNavigated(SectionContentFrame(
                self.window, sectionData=sectionData, name=text))
        for key in self.sections:
            Button(self, text=key, command=lambda key=key: createSectionContentFrame(
                text=key, sectionData=self.sections[key]))

    def setAllButtonSizeRelativeToScreen(self, defaultWidgetSize: float) -> None:
        widthSize = int(self.window.getWidth() * defaultWidgetSize)
        heightSize = int(self.window.getHeight() * defaultWidgetSize)
        for widget in self.winfo_children():
            if isinstance(widget, Button):
                widthUnit, heightUnit = convertPixelsToTextUnit(
                    widget, widthSize, heightSize)
                widget.config(width=widthUnit, height=heightUnit)

    def _gridPlacement(self) -> None:
        buttonCount = 0
        for widget in self.winfo_children():
            if isinstance(widget, Button):
                widget.grid(row=buttonCount, column=0)
                buttonCount += 1

    def _setGridProperties(self) -> None:
        self.grid_propagate(False)
        self.grid_anchor(CENTER)
