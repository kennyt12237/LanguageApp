from tkinter import Misc

from ..AbstractFrame import TableGridFrame


class GrammarFrame(TableGridFrame):

    def __init__(self, master: Misc, grammarData: list[dict[str, str]] = None, **kwargs) -> None:
        super().__init__(master, grammarData, **kwargs)

    def _setGridProperties(self) -> None:
        self.grid_propagate(False)
