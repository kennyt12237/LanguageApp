from tkinter import Frame, Label, CENTER
from ..Window import Window
from .GridFrame import GridFrame
import json

class DictionaryFrame(GridFrame):
    
    def __init__(self, window : Window, data : json = None, name : str = "Dictionary"):
        super().__init__(window, name, width=window.getWidthMinusPadding(), height=int(window.getHeight() * 0.5), background="green")
        self.dictionary : list[dict[str,str]] = json.loads(data)
        self._createLabels()
        
    def _createLabels(self) -> None:
        labelCount = 0
        for entry in self.dictionary:
            labelText = ""
            for values in entry.values():
                if len(labelText) > 0:
                    labelText += " "
                labelText += values.strip()
            Label(self, text=labelText).grid(row=labelCount, column=0)
            labelCount = labelCount + 1
        
    def getName(self) -> None:
        return self.name