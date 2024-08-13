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
            Label(self, text=header.strip().capitalize(), borderwidth=2, relief="groove").grid(row=0, column=headerCount, sticky="nsew")
            headerCount += 1
        
        labelCount = 0
        for entry in self.dictionary:
            labelIndex = 0
            for values in entry.values():
                Label(self, text=values.strip(), borderwidth=2, relief="groove").grid(row=labelCount + 1, column=labelIndex, sticky="nsew")
                labelIndex += 1
            labelCount = labelCount + 1
        self._additionalGridProperties(labelCount + 1, headerCount)
            
    def _setGridProperties(self) -> None:
        self.grid_propagate(False)
        
    def _additionalGridProperties(self, row : int, col : int) -> None:
        self.grid_rowconfigure(0, weight = 2)
        for i in range(1,row):
            self.grid_rowconfigure(i, weight=1)
        
        for j in range(col):
            self.grid_columnconfigure(j, weight=1)