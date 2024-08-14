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
        self.buttons : list[Button] = self._createButtons()
        print("Buttons", self.buttons)
        self._setButtonProperties()
        
    def createSectionContentFrame(self, text, sectionData) -> None:
        self.window.newFrameNavigated(SectionContentFrame(self.window, name=text, sectionData=sectionData))
            
    def _createButtons(self) -> list[Button]:
        buttonList : list[Button] = []
        buttonCount = 0
        for key in self.sections:
            button = Button(self, text=key, command=lambda key=key: self.createSectionContentFrame(text=key,sectionData = self.sections[key]))
            button.grid(row=buttonCount, column=0)
            buttonList.append(button)
            buttonCount = buttonCount + 1
        return buttonList
    
    def _setButtonProperties(self) -> None:
        widthSize = int(self.window.getWidth() * self.defaultWidgetSize)
        heightSize = int(self.window.getHeight() * self.defaultWidgetSize)
        for button in self.buttons:
            widthUnit, heightUnit = convertPixelsToTextUnit(button, widthSize, heightSize)
            button.config(width=widthUnit, height=heightUnit)
            
    def _setGridProperties(self) -> None:
        self.grid_anchor(CENTER)
