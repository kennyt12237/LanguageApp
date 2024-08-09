from tkinter import Frame, Misc
from tkinter import CENTER

class GridFrame(Frame):
    
    def __init__(self, master : Misc, **kwargs) -> None:
        super().__init__(master, kwargs)
        self._setGridProperties()
    
    def setGridRowAndColumn(self, row : int, column : int) -> None:
        self.row = row
        self.column = column
        
    def _setGridProperties(self) -> None:
        pass
