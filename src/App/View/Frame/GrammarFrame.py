from tkinter import Label, Misc
import json

from .AbstractFrame import TableGridFrame
from .Styling import getTableHeaderLabelSettings, getTableLabelSettings


class GrammarFrame(TableGridFrame):

    def __init__(self, master: Misc, grammarData: list[dict[str, str]] = None, **kwargs) -> None:
        headerStyling = getTableHeaderLabelSettings()
        entryStyling = getTableLabelSettings()
        super().__init__(master, grammarData, headerStyling, entryStyling, **kwargs)

    def _setGridProperties(self) -> None:
        self.grid_propagate(False)