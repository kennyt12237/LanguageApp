from tkinter import Label, Misc
from .GridFrame import GridFrame
from .Styling import getDictionaryHeaderLabelSettings, getDictionaryLabelSettings
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
            Label(self, text=header.strip().capitalize(), **getDictionaryHeaderLabelSettings()).grid(row=0, column=headerCount, sticky="nsew")
            headerCount += 1
        
        labelCount = 1
        for entry in self.dictionary:
            labelIndex = 0
            for values in entry.values():
                Label(self, text=values.strip(), **getDictionaryLabelSettings()).grid(row=labelCount, column=labelIndex, sticky="nsew")
                labelIndex += 1
            labelCount = labelCount + 1
        self._additionalGridProperties(labelCount, headerCount)
        
    def _additionalGridProperties(self, row : int, col : int) -> None:
        self.grid_rowconfigure(0, minsize=100)
        for i in range(1,row):
            self.grid_rowconfigure(i, minsize=50)
        
        for j in range(col):
            self.grid_columnconfigure(j, weight=1)