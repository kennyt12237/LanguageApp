from tkinter import Misc, Label
from tkinter import CENTER
from .TkinterWidget import GridFrame

from .styling import defaultNoContentLabel

class NoContentFrame(GridFrame):

    NO_CONTENT = "No Content"

    def __init__(self, master: Misc, text: str = NO_CONTENT, **kwargs) -> None:
        super().__init__(master, **kwargs)
        self.noContentLabel = Label(self, text=text, **defaultNoContentLabel)
        self._gridPlacement()

    def _setGridProperties(self) -> None:
        self.grid_anchor(CENTER)

    def _gridPlacement(self) -> None:
        self.noContentLabel.grid(row=0, column=0, sticky="nsew")
        self.noContentLabel.grid_rowconfigure(0, weight=1)
        self.noContentLabel.grid_columnconfigure(0, weight=1)
