from tkinter import Button, Misc
from tkinter import CENTER
import json

from ..Window import Window
from ..Utils import convertPixelsToTextUnit
from .SectionContentFrame import SectionContentFrame
from .GridFrame import GridFrame

class SectionFrame(GridFrame):
    
    def __init__(self, master : Misc, data : json = None, defaultWidgetSize : float = 0.1, name : str = "section", **kwargs) -> None:
        kwargs["name"] = name
        super().__init__(master, **kwargs)
        self.defaultWidgetSize = defaultWidgetSize
        self.window : Window = self.winfo_toplevel()
        self.sections = json.loads(data)
        self._createButtons()
        self._setButtonProperties()
        self._gridPlacement()
        
    def createSectionContentFrame(self, text, sectionData) -> None:
        self.window.newFrameNavigated(SectionContentFrame(self.window, name=text, sectionData=sectionData))
            
    def _createButtons(self) -> None:
        for key in self.sections:
            button = Button(self, text=key, command=lambda key=key: self.createSectionContentFrame(text=key,sectionData = self.sections[key]))

    def _setButtonProperties(self) -> None:
        widthSize = int(self.window.getWidth() * self.defaultWidgetSize)
        heightSize = int(self.window.getHeight() * self.defaultWidgetSize)
        for widget in self.winfo_children():
            if isinstance(widget,Button):
                widthUnit, heightUnit = convertPixelsToTextUnit(widget, widthSize, heightSize)
                widget.config(width=widthUnit, height=heightUnit)
            
    def _setGridProperties(self) -> None:
        self.grid_anchor(CENTER)

    def _gridPlacement(self) -> None:
        buttonCount = 0
        for widget in self.winfo_children():
            if isinstance(widget, Button):
                widget.grid(row=buttonCount, column=0)
                buttonCount += 1