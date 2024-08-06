from tkinter import Frame, Button
import json

from ..Window import Window
from .SectionContentFrame import SectionContentFrame
from ..Utils import packAllChildWidgets, packForgetAllChildWidgets

class SectionFrame(Frame):
    
    def __init__(self, window : Window, data : json = None, name : str = "Section") -> None:
        super().__init__(window)
        self.window = window
        self.sections = json.loads(data)
        self.name = name
        self._createButtons()
        
    def createSectionContentFrame(self, text, sectionData) -> None:
        self.window.newFrameNavigated(SectionContentFrame(self.window, title=text, sectionData=sectionData))
            
    def _createButtons(self) -> None:
        buttonCount = 0
        for key in self.sections:
            Button(self, text=key, command=lambda key=key: self.createSectionContentFrame(text=key,sectionData = self.sections[key])).grid(row=buttonCount, column=0)
            buttonCount = buttonCount + 1
    
    def getName(self) -> None:
        return self.name