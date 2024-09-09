from .SentenceLabelSize import SentenceLabelSize
from .SymbolLabelToggle import DictionaryTooltipToggle, GrammarTooltipToggle
from ....Section import GridFrame


class SentenceFrame(GridFrame):

    def __init__(self, master, **kwargs) -> None:
        super().__init__(master, **kwargs)
        self.sentenceLabelSize = SentenceLabelSize(self)
        self.dictionaryWordToggle = DictionaryTooltipToggle(self)
        self.grammarTooltipToggle = GrammarTooltipToggle(self)
        self._gridPlacement()

    def _gridPlacement(self) -> None:
        self.sentenceLabelSize.grid(row=0, column=0, sticky="nsew")
        self.dictionaryWordToggle.grid(row=1, column=0, sticky="nsew")
        self.grammarTooltipToggle.grid(row=2, column=0, sticky="nsew")
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_columnconfigure(0, weight=1)
