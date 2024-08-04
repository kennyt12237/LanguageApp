from tkinter import Frame, Button
from .WidgetUtils import packAllChildWidgets, packForgetAllChildWidgets
from .Window import Window
from .SectionContentFrame import SectionContentFrame
import json

class SectionFrame(Frame):
    
    def __init__(self, window : Window, data : json = None) -> None:
        super().__init__(window)
        self.window = window
        self.sections = json.loads(data)
        self._createButtons()
        
    def createSectionContentFrame(self, text, sectionData) -> None:
        self.window.newFrameNavigated(SectionContentFrame(self.window, title=text, sectionData=sectionData))
            
    def _createButtons(self) -> None:
        for key in self.sections:
            Button(self, text=key, command=lambda key=key: self.createSectionContentFrame(text=key,sectionData = self.sections[key]))
    
    def pack(self) -> None:
        packAllChildWidgets(self)
        super().pack()
        
    def pack_forget(self) -> None:
        packForgetAllChildWidgets(self)
        super().pack_forget()