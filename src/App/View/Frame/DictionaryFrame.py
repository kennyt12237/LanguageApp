from tkinter import Frame, Label
import json

class DictionaryFrame(Frame):
    
    def __init__(self, window, data : json = None, name : str = "Dictionary"):
        super().__init__(window)
        self.name = name
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