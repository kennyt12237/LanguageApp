from .SentenceLabelSize import SentenceLabelSize
from .DictionaryWordToggle import DictionaryWordToggle
from ....Section import GridFrame


class SentenceFrame(GridFrame):

    def __init__(self, master, **kwargs) -> None:
        super().__init__(master, **kwargs)
        self.sentenceLabelSize = SentenceLabelSize(self)
        self.dictionaryWordToggle = DictionaryWordToggle(self)
        self._gridPlacement()

    def _gridPlacement(self) -> None:
        self.sentenceLabelSize.grid(row=0, column=0, sticky="nsew")
        self.dictionaryWordToggle.grid(row=1, column=0, sticky="nsew")
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)
