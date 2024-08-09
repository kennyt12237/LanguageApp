from tkinter import Button, Misc
import json

from ..Window import Window
from .SectionContentFrame import SectionContentFrame
from .GridFrame import GridFrame

class SectionFrame(GridFrame):
    
    def __init__(self, master : Misc, window : Window, data : json = None, name : str = "section") -> None:
        super().__init__(master, window, name=name, width=window.getWidthMinusPadding(), height=int(window.getHeight() * 0.5), background="green")
        self.sections = json.loads(data)
        self._createButtons()
        
    def createSectionContentFrame(self, text, sectionData) -> None:
        self.window.newFrameNavigated(SectionContentFrame(self.window, self.window, title=text, sectionData=sectionData))
            
    def _createButtons(self) -> None:
        buttonCount = 0
        for key in self.sections:
            Button(self, text=key, command=lambda key=key: self.createSectionContentFrame(text=key,sectionData = self.sections[key])).grid(row=buttonCount, column=0)
            buttonCount = buttonCount + 1