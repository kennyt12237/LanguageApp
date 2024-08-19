from tkinter import Label, Misc
from .GridFrame import GridFrame
from .Styling import getTableHeaderLabelSettings, getTableLabelSettings
import json

class DictionaryFrame(GridFrame):
    
    def __init__(self, master : Misc, data : json = None, name : str = "dictionary", **kwargs):
        kwargs["name"] = name
        super().__init__(master, **kwargs)
        self.dictionary : list[dict[str,str]] = json.loads(data)
        self._createLabels()
    
    def _createLabels(self) -> None:
        headerList = list(self.dictionary[0].keys())
        headerItemCount = 0
        headerLabelSettings = getTableHeaderLabelSettings()
        Label(self, text="Number", **headerLabelSettings,).grid(row=0, column=headerItemCount, sticky="nsew")
        headerItemCount += 1
        for header in headerList:
            Label(self, text=header.strip().capitalize(), **headerLabelSettings).grid(row=0, column=headerItemCount, sticky="nsew")
            headerItemCount += 1
        
        labelCount = 1
        labelSettings = getTableLabelSettings()
        for entry in self.dictionary:
            labelIndex = 0
            background = '#d7f1f7' if labelCount % 2 == 0 else self.cget('bg')
            Label(self,text=labelCount, background=background, **labelSettings).grid(row=labelCount, column=labelIndex, sticky="nsew")
            labelIndex += 1
            for values in entry.values():
                Label(self, text=values.strip(), background=background, **labelSettings).grid(row=labelCount, column=labelIndex, sticky="nsew")
                labelIndex += 1
            labelCount = labelCount + 1
        self._additionalGridProperties(labelCount, headerItemCount)

    def _setGridProperties(self) -> None:
        self.grid_propagate(False)
        
    def _additionalGridProperties(self, row : int, col : int) -> None:
        self.grid_rowconfigure(0, minsize=100)
        for i in range(1,row):
            self.grid_rowconfigure(i, minsize=75)
        
        for j in range(col):
            self.grid_columnconfigure(j, weight=1)