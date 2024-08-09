from tkinter import Frame, Misc
from tkinter import CENTER
from ..Window import Window

class GridFrame(Frame):
    
    def __init__(self, master : Misc, window : Window, **kwargs) -> None:
        self.window = window
        super().__init__(master, kwargs)
        self._setGridProperties()
    
    def _setGridProperties(self) -> None:
        pass