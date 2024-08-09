from tkinter import Button, Misc
import json

from ..Window import Window
from .SectionContentFrame import SectionContentFrame
from .GridFrame import GridFrame

class SectionFrame(GridFrame):
    
    def __init__(self, master : Misc, data : json = None, name : str = "section", **kwargs) -> None:
        kwargs["name"] = name
        super().__init__(master, **kwargs)
        self.window : Window = self.winfo_toplevel()
        self.sections = json.loads(data)
        self._createButtons()
        
    def createSectionContentFrame(self, text, sectionData) -> None:
        self.window.newFrameNavigated(SectionContentFrame(self.window, name=text, sectionData=sectionData))
            
    def _createButtons(self) -> None:
        buttonCount = 0
        for key in self.sections:
            Button(self, text=key, command=lambda key=key: self.createSectionContentFrame(text=key,sectionData = self.sections[key])).grid(row=buttonCount, column=0)
            buttonCount = buttonCount + 1