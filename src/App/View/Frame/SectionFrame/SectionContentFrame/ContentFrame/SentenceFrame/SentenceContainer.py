from tkinter import Misc

from ..AbstractFrame import GridFrame
from .SentenceDataFrame import SentenceDataFrame
from .SentenceNavigationFrame import SentenceNavigationFrame
from .Utils import TkManager

import json

class SentenceContainer(GridFrame):

    STICKY = "nsew"

    def __init__(self, master: Misc, sentenceData: list[dict[str, str]], grammarData: list[dict[str, str]] = None, initIndex: int = 0, **kwargs) -> None:
        super().__init__(master, **kwargs)
        self.initIndex = initIndex
        self.sentenceData: list[dict[str, str]] = json.loads(sentenceData)
        self.grammars: list[str] = grammarData
        self.sentenceDataFrame = SentenceDataFrame(self, self.grammars)
        self.sentenceNavigationFrame = SentenceNavigationFrame(
            self, self.initIndex + 1, len(self.sentenceData), self.changeSentenceDataFrame)
        self.__setInitialSentenceFrameData(0)
        self._gridPlacement()

    def __setInitialSentenceFrameData(self, index) -> None:
        self.changeSentenceDataFrame(index)
        
    def changeSentenceDataFrame(self, nextIndex: int) -> None:
        nextSentence = self._getSentenceDataIndexSentence(nextIndex)
        nextMeaning = self._getSentenceDataIndexMeaning(nextIndex)
        self.sentenceDataFrame.changeLabelTexts(nextSentence, nextMeaning, TkManager.PLACE)

    def _getSentenceDataIndex(self) -> list[str]:
        return list(self.sentenceData[0].values())

    def _getSentenceDataIndexSentence(self, index: int) -> str:
        return list(self.sentenceData[index].values())[0]

    def _getSentenceDataIndexMeaning(self, index: int) -> str:
        return list(self.sentenceData[index].values())[1]

    def _gridPlacement(self) -> None:
        self.sentenceDataFrame.grid(row=0, column=0, sticky=self.STICKY)
        self.sentenceNavigationFrame.grid(row=1, column=0, sticky=self.STICKY)
        self.grid_rowconfigure(0, weight=11)
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)

    def _setGridProperties(self) -> None:
        self.grid_propagate(False)