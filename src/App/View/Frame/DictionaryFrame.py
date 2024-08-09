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
        headerList = list(self.dictionary[0].keys())
        headerCount = 0
        for header in headerList:
            Label(self, text=header.strip().capitalize()).grid(row=0, column=headerCount)
            headerCount += 1
        
        labelCount = 0
        for entry in self.dictionary:
            labelIndex = 0
            for values in entry.values():
                Label(self, text=values.strip()).grid(row=labelCount + 1, column=labelIndex)
                labelIndex += 1
            labelCount = labelCount + 1
        self._additionalGridProperties(labelCount + 1, headerCount)
            
    def _additionalGridProperties(self, row : int, col : int) -> None:
        for i in range(row):
            self.grid_rowconfigure(i, weight=1)
        
        for j in range(col):
            self.grid_columnconfigure(j, weight=1)