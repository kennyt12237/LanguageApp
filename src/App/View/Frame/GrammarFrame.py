from tkinter import Label, Misc
import json

from .AbstractFrame.GridFrame import GridFrame
from .Styling import getTableHeaderLabelSettings, getTableLabelSettings

class GrammarFrame(GridFrame):
    
    GRID_STICKY = "nsew"
    
    def __init__(self, master : Misc, grammarData : list[dict[str,str]] = None, name : str = "grammar", **kwargs) -> None:
        kwargs["name"] = name
        super().__init__(master, **kwargs)
        self.grammarData : list[dict[str,str]] = json.loads(grammarData)
        self._createLabels(self.grammarData)
        
    def _createLabels(self, grammarData : list[dict[str,str]] = None) -> None:
        tableHeaderSettings = getTableHeaderLabelSettings()
        tableLabelSettings = getTableLabelSettings()
        headerCount = 0
        for header in grammarData[0].keys():
            Label(self, text=header.capitalize(), **tableHeaderSettings).grid(row=0, column=headerCount, sticky=self.GRID_STICKY)
            headerCount += 1
        labelCount = 1
        for grammar in grammarData:
            columnPlace = 0
            for value in grammar.values():
                Label(self, text=str(value).strip(), **tableLabelSettings).grid(row=labelCount, column=columnPlace, sticky=self.GRID_STICKY)
                columnPlace += 1
            labelCount = labelCount + 1
        self._additionalGridProperties(labelCount, headerCount)
        
    def _setGridProperties(self) -> None:
        self.grid_propagate(False)
        
    def _additionalGridProperties(self, row : int, column : int) -> None:
        self.grid_rowconfigure(0, minsize=100)
        for rowCount in range(1,row):
            self.grid_rowconfigure(rowCount, minsize=75)
            
        for colCount in range(0, column):
            self.grid_columnconfigure(colCount, weight=1)