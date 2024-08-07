from tkinter import Frame, CENTER
from ..Window import Window

class GridFrame(Frame):
    
    def __init__(self, window : Window, name : str, **kwargs) -> None:
        self.window = window
        self.name = name
        super().__init__(window, kwargs)
        self._setGridProperties()
    
    def _setGridProperties(self) -> None:
        self.grid_propagate(False)
        self.grid_anchor(CENTER)
        
    def getName(self) -> str:
        return self.name