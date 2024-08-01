from .WidgetUtils import packAllChildWidgets, packForgetAllChildWidgets

from tkinter import Frame, Label
import json

class DictionaryFrame(Frame):
    
    def __init__(self, window, data : json = None):
        super().__init__(window)
        self.dictionary : list[dict[str,str]] = json.loads(data)
        self._createLabels()
        
    def _createLabels(self) -> None:
        for entry in self.dictionary:
            labelText = ""
            for values in entry.values():
                if len(labelText) > 0:
                    labelText += " "
                labelText += values.strip()
            Label(self, text=labelText)
        
    def pack(self) -> None:
        packAllChildWidgets(self)
        super().pack()
        
    def pack_forget(self) -> None:
        packForgetAllChildWidgets(self)
        super().pack_forget()