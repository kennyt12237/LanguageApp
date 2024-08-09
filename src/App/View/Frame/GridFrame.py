from tkinter import Frame, Misc
from tkinter import CENTER
from ..Window import Window

class GridFrame(Frame):
    
    def __init__(self, master : Misc, window : Window, name : str, **kwargs) -> None:
        self.window = window
        self.name = name
        super().__init__(master, kwargs)
        self._setGridProperties()
    
    def _setGridProperties(self) -> None:
        pass
        
    def getName(self) -> str:
        return self.name