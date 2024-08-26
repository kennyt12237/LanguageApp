from tkinter import Misc
from ..AbstractFrame import TableGridFrame
import json


class DictionaryFrame(TableGridFrame):

    def __init__(self, master: Misc, data: json = None, **kwargs):
        super().__init__(master, data, **kwargs)

    def _setGridProperties(self) -> None:
        self.grid_propagate(False)
