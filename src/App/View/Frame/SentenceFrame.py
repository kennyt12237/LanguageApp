from tkinter import Frame, Label, Button, Misc, Event
from tkinter import CENTER, LEFT, S, N
from typing import Callable
import json

from .Styling import getSentenceTextFont, getSentenceMeaningFont, getStepLabelFont
from .AbstractFrame import GridFrame
from ..Utils import getGrammarCharactersList, getGrammarDataFromCharacter


class SentenceContainer(GridFrame):

    STICKY = "nsew"

    def __init__(self, master: Misc, sentenceData: list[dict[str, str]], grammarData: list[dict[str, str]] = None, initIndex: int = 0, **kwargs) -> None:
        super().__init__(master, **kwargs)
        self.initIndex = initIndex
        self.sentenceData: list[dict[str, str]] = json.loads(sentenceData)
        self.grammars: list[str] = grammarData
        self.sentenceDataFrame = SentenceDataFrame(self, self._getSentenceDataIndexSentence(
            self.initIndex), self._getSentenceDataIndexMeaning(self.initIndex), self.grammars)
        self.sentenceNavigationFrame = SentenceNavigationFrame(
            self, self.initIndex + 1, len(self.sentenceData), self.changeSentenceDataFrame)
        self._gridPlacement()

    def changeSentenceDataFrame(self, nextIndex: int) -> None:
        nextSentence = self._getSentenceDataIndexSentence(nextIndex)
        nextMeaning = self._getSentenceDataIndexMeaning(nextIndex)
        self.sentenceDataFrame.changeLabelTexts(nextSentence, nextMeaning)

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


class SentenceDataFrame(GridFrame):

    def __init__(self, rootFrame: Frame, sentence: str = None, meaning: str = None, grammarData: list[dict[str,str]] = None, **kwargs) -> None:
        super().__init__(rootFrame, **kwargs)
        self.rootFrame = rootFrame
        self.sentence = sentence
        self.meaning = meaning
        self.grammarData = grammarData
        self.sentenceFrame = SentenceFrameWrapper(
            self, self.sentence, font=getSentenceTextFont(), grammarData=self.grammarData)
        self.meaningLabel = Label(
            self, text=meaning, font=getSentenceMeaningFont())
        self._gridPlacement()

    def changeLabelTexts(self, sentence: str = None, meaning: str = None) -> None:
        self.sentenceFrame.changeLabels(text=sentence)
        self.meaningLabel.config(text=meaning)

    def _gridPlacement(self) -> None:
        self.sentenceFrame.grid(row=0, column=0, pady=(0, 40), sticky="nsew")
        self.meaningLabel.grid(row=1, column=0, sticky=N)

    def _setGridProperties(self) -> None:
        self.grid_anchor(CENTER)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)
        
class SentenceFrameWrapper(Frame):
    
    def __init__(self, master: Misc, text: str, font: tuple = None, grammarData: list[dict[str,str]] = None, **kwargs) -> None:
        super().__init__(master, **kwargs)
        self.sentenceFrame = SentenceFrame(self, text, font, grammarData, **kwargs)
        self.sentenceFrame.pack(side="bottom")
        
    def changeLabels(self, text: str) -> None:
        self.sentenceFrame.changeLabels(text)
        
class SentenceFrame(Frame):

    BACKGROUND_COLOR = 'yellow'

    def __init__(self, master: Misc, text: str, font: tuple = None, grammarData: list[dict[str,str]] = None, **kwargs) -> None:
        super().__init__(master, **kwargs)
        self.font = font
        self.grammarData = grammarData
        self.characters : list[str] = getGrammarCharactersList(grammarData)
        self.changeLabels(text=text)
        
    def _createLabels(self, text: str) -> None:
        for char in text:
            if char in self.characters:
                label = LabelWithTooltip(self, tooltipParent=self.master, text=char, font=self.font,
                              background=self.BACKGROUND_COLOR)
                grammar = getGrammarDataFromCharacter(self.grammarData, char)
                yOffset = 100
                label.setToolTip(grammar=grammar, yOffset=yOffset)
            else:
                Label(self, text=char, font=self.font)

    def _removeAllLabels(self) -> None:
        for label in self.winfo_children():
            label.destroy()

    def _packAllLabels(self) -> None:
        for label in self.winfo_children():
            label.pack(side=LEFT, anchor=S)

    def changeLabels(self, text: str) -> None:
        self._removeAllLabels()
        self._createLabels(text=text)
        self._packAllLabels()


class LabelWithTooltip(Label):

    def __init__(self, master : Misc, tooltipParent : Misc, **kwargs) -> None:
        super().__init__(master, **kwargs)
        self.tooltipParent = tooltipParent
        self.toolTip : Label = None

    def setToolTip(self, grammar: dict[str, str], yOffset : int = 0) -> None:
        self.bind("<Enter>", func=lambda e: self.__createTooltip(grammar, yOffset))
        self.bind("<Leave>", func=lambda e: self.__removeToolTip())

    def __createTooltip(self, grammar: dict[str, str], yOffset : int) -> None:
        text = "Pinyin : {pinyin}\nCharacter : {character}{num}\nMeaning : {meaning}".format(
            pinyin=grammar["pinyin"],
            character=grammar["character"],
            num=grammar["number"],
            meaning=grammar["usage"])
        self.toolTip = Label(self.tooltipParent, text=text, borderwidth=2, padx=10, pady=10, relief="solid", background="lightyellow")
        # print(self.master, self.master.winfo_width(), self.master.winfo_height())
        # print(self.tooltipParent, self.tooltipParent.winfo_width(), self.tooltipParent.winfo_height())
        # print(self.toolTip, self.toolTip.winfo_reqwidth(), self.toolTip.winfo_reqheight())
        xPos = self.master.winfo_x() + self.winfo_x() - (self.toolTip.winfo_reqwidth() / 2)
        yPos = self.tooltipParent.winfo_height() - self.master.winfo_height() - self.toolTip.winfo_reqheight() - 20
        self.toolTip.place(x=xPos, y=yPos)
        
    def __removeToolTip(self) -> None:
        self.toolTip.destroy()

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
