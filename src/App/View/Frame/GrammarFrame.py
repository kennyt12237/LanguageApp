from tkinter import Label, Misc
import json

from .GridFrame import GridFrame

class GrammarFrame(GridFrame):
    
    def __init__(self, master : Misc, grammarData : list[dict[str,str]] = None, name : str = "grammar", **kwargs) -> None:
        kwargs["name"] = name
        super().__init__(master, **kwargs)
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