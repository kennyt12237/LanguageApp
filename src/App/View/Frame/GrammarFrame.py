from tkinter import Frame, Label
import json

from .GridFrame import GridFrame
from ..Window import Window

class GrammarFrame(GridFrame):
    
    def __init__(self, window : Window, grammarData : list[dict[str,str]] = None, name : str = "Grammar") -> None:
        super().__init__(window, name, width=window.getWidthMinusPadding(), height=int(window.getHeight() * 0.5), background="green")
        self.grammarData : list[dict[str,str]] = json.loads(grammarData)
        self._createLabels(self.grammarData)
        
    def _createLabels(self, grammarData : list[dict[str,str]] = None) -> None:
        labelCount = 0
        for grammar in grammarData:
            labelText = ""
            for value in grammar.values():
                if len(labelText) > 0:
                    labelText += " "
                labelText += str(value).strip()
            Label(self, text=labelText).grid(row=labelCount, column=0)
            labelCount = labelCount + 1