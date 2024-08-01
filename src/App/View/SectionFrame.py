from tkinter import Frame, Button
from .WidgetUtils import packAllChildWidgets, packForgetAllChildWidgets
import json

class SectionFrame(Frame):
    
    def __init__(self, window, data : json = None) -> None:
        super().__init__(window)
        self.sections = json.loads(data)
        self._createButtons()
        
    def _createButtons(self) -> None:
        for key in self.sections:
            Button(self, text=key)
    
    def pack(self) -> None:
        packAllChildWidgets(self)
        super().pack()
        
    def pack_forget(self) -> None:
        packForgetAllChildWidgets(self)
        super().pack_forget()