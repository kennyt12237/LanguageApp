from tkinter import Label, Misc
from .GridFrame import GridFrame
import json

class DictionaryFrame(GridFrame):
    
    def __init__(self, master : Misc, data : json = None, name : str = "dictionary", **kwargs):
        kwargs["name"] = name
        super().__init__(master, **kwargs)
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