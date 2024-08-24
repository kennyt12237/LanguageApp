from tkinter import Frame, Label, Button
from typing import Callable

from ..Styling import getStepLabelFont
from ..AbstractFrame import GridFrame

class SentenceNavigationFrame(GridFrame):

    PREVIOUS = "Previous"
    NEXT = "Next"
    STICKY = "nsew"

    def __init__(self, rootFrame: Frame, initIndex: int = 1, totalSentences: int = 1, callback: Callable = None, **kwargs) -> None:
        super().__init__(rootFrame, **kwargs)
        self.rootFrame = rootFrame
        self.currentIndex = initIndex
        self.totalSentences = totalSentences
        self.callback = callback
        self.previousButton = Button(
            self, text=self.PREVIOUS, command=self.onPreviousButtonPressed)
        self.stepLabel = Label(self, text=self._regenerateStepLabelText(
            self.currentIndex, totalSentences), font=getStepLabelFont())
        self.nextButton = Button(self, text=self.NEXT,
                                 command=self.onNextButtonPressed)
        self._determineButtonVisibility()
        self._gridPlacement()

    def onPreviousButtonPressed(self) -> None:
        if self.currentIndex > 1:
            previousIndex = self.currentIndex - 1
            self.callback(previousIndex - 1)
            self.currentIndex = previousIndex
            self._changeStepLabelText(previousIndex, self.totalSentences)
            self._determineButtonVisibility()

    def onNextButtonPressed(self) -> None:
        if self.currentIndex < self.totalSentences:
            nextIndex = self.currentIndex + 1
            self.callback(nextIndex - 1)
            self.currentIndex = nextIndex
            self._changeStepLabelText(nextIndex, self.totalSentences)
            self._determineButtonVisibility()

    def _regenerateStepLabelText(self, currentIndex: int = 1, totalSentence: int = 1) -> str:
        return "{currentIndex} of {totalSentence}".format(currentIndex=currentIndex, totalSentence=totalSentence)

    def _changeStepLabelText(self, nextIndex: int, totalSentence: int) -> None:
        self.stepLabel.config(
            text=self._regenerateStepLabelText(nextIndex, totalSentence))

    def __previousButtonVisibility(self) -> None:
        if self.currentIndex <= 1:
            self.previousButton.grid_remove()
            return
        self.previousButton.grid(row=0, column=0, sticky=self.STICKY)

    def __nextButtonVisibility(self) -> None:
        if self.currentIndex >= self.totalSentences:
            self.nextButton.grid_remove()
            return
        self.nextButton.grid(row=0, column=2, sticky=self.STICKY)

    def _determineButtonVisibility(self) -> None:
        self.__previousButtonVisibility()
        self.__nextButtonVisibility()

    def _gridPlacement(self) -> None:
        self.stepLabel.grid(row=0, column=1)
        self.grid_columnconfigure(0, weight=1, minsize=100)
        self.grid_columnconfigure(1, weight=10)
        self.grid_columnconfigure(2, weight=1, minsize=100)
        self.grid_rowconfigure(0, weight=1)

    def _setGridProperties(self) -> None:
        self.grid_propagate(False)
