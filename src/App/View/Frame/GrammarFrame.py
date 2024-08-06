from tkinter import Frame, Label
import json

from ..Window import Window
from ..Utils import packAllChildWidgets, packForgetAllChildWidgets

class GrammarFrame(Frame):
    
    def __init__(self, window : Window, grammarData : list[dict[str,str]] = None) -> None:
        super().__init__(window)
        self.window : Window = window
        self.grammarData : list[dict[str,str]] = json.loads(grammarData)
        self._createLabels(self.grammarData)
        
    def _createLabels(self, grammarData : list[dict[str,str]] = None) -> None:
        for grammar in grammarData:
            labelText = ""
            for value in grammar.values():
                if len(labelText) > 0:
                    labelText += " "
                labelText += str(value).strip()
            Label(self, text=labelText)
        
    def pack(self) -> None:
        packAllChildWidgets(self)
        super().pack()
        
    def pack_forget(self) -> None:
        packForgetAllChildWidgets(self)
        super().pack_forget()