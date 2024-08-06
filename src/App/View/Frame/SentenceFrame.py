from tkinter import Frame, Label, Button
from typing import Callable
import json

from ..Window import Window

class SentenceFrame(Frame):
    
    def __init__(self, window : Window, sentenceData : list[dict[str,str]] = None, initIndex : int = 0, name : str = "Sentences") -> None:
        super().__init__(window)
        self.window = window
        self.initIndex = initIndex
        self.sentenceData : list[dict[str,str]] = json.loads(sentenceData)
        self.name = name
        self.sentenceDataFrame = SentenceDataFrame(self, self._getSentenceDataIndexSentence(self.initIndex), self._getSentenceDataIndexMeaning(self.initIndex))
        self.sentenceNavigationFrame = SentenceNavigationFrame(self, self.initIndex + 1, len(self.sentenceData), self.changeSentenceDataFrame)
        self.sentenceDataFrame.grid(row=0, column=0)
        self.sentenceNavigationFrame.grid(row=1, column=0)
        
    def changeSentenceDataFrame(self, nextIndex : int) -> None:
        nextSentence = self._getSentenceDataIndexSentence(nextIndex)
        nextMeaning = self._getSentenceDataIndexMeaning(nextIndex)
        self.sentenceDataFrame.changeLabelTexts(nextSentence, nextMeaning)
        
    def _getSentenceDataIndex(self) -> list[str]:
        return list(self.sentenceData[0].values())
    
    def _getSentenceDataIndexSentence(self, index : int) -> str:
        return list(self.sentenceData[index].values())[0]
    
    def _getSentenceDataIndexMeaning(self, index : int) -> str:
        return list(self.sentenceData[index].values())[1]

    def getName(self) -> None:
        return self.name
    
class SentenceDataFrame(Frame):
    
    def __init__(self, rootFrame : Frame, sentence : str = None, meaning : str = None) -> None:
        super().__init__(rootFrame)
        self.rootFrame = rootFrame
        self.sentence = sentence
        self.meaning = meaning
        self.sentenceLabel = Label(self, text=sentence)
        self.meaningLabel = Label(self, text=meaning)
        self.sentenceLabel.grid(row=0, column=0)
        self.meaningLabel.grid(row=1, column=0)
        
    def changeLabelTexts(self, sentence : str = None, meaning : str = None) -> None:
        self.sentenceLabel.config(text=sentence)
        self.meaningLabel.config(text=meaning)
        
class SentenceNavigationFrame(Frame):
    
    def __init__(self, rootFrame : Frame, initIndex : int = 1, totalSentences : int = 1, callback : Callable = None) -> None:
        super().__init__(rootFrame)
        self.rootFrame = rootFrame
        self.currentIndex = initIndex
        self.totalSentences = totalSentences
        self.callback = callback
        self.previousButton = Button(self, text="Previous", command=self._onPreviousButtonPressed)
        self.stepLabel = Label(self, text=self._regenerateStepLabelText(self.currentIndex, totalSentences))
        self.nextButton = Button(self, text="Next", command=self._onNextButtonPressed)
        self.stepLabel.grid(row=0, column=1)
        self._determineButtonVisibility()
        
    def _regenerateStepLabelText(self, currentIndex : int = 1, totalSentence : int = 1) -> str:
        return "{currentIndex} of {totalSentence}".format(currentIndex=currentIndex, totalSentence=totalSentence)
    
    def _changeStepLabelText(self, nextIndex : int, totalSentence : int) -> None:
        self.stepLabel.config(text=self._regenerateStepLabelText(nextIndex, totalSentence))
        
    def _onPreviousButtonPressed(self) -> None:
        if self.currentIndex > 1:
            previousIndex = self.currentIndex - 1
            self.callback(previousIndex - 1)
            self.currentIndex = previousIndex
            self._changeStepLabelText(previousIndex, self.totalSentences)
            self._determineButtonVisibility()
            
    def _onNextButtonPressed(self) -> None:
        if self.currentIndex < self.totalSentences:
            nextIndex = self.currentIndex + 1
            self.callback(nextIndex - 1)
            self.currentIndex = nextIndex
            self._changeStepLabelText(nextIndex, self.totalSentences)
            self._determineButtonVisibility()
            
    def __previousButtonVisibility(self) -> None:
        if self.currentIndex <= 1:
            self.previousButton.grid_forget()
            return
        self.previousButton.grid(row=0, column=0)
        
    def __nextButtonVisibility(self) -> None:
        if self.currentIndex >= self.totalSentences:
            self.nextButton.grid_forget()
            return
        self.nextButton.grid(row=0, column=2)
            
    def _determineButtonVisibility(self) -> None:
        self.__previousButtonVisibility()
        self.__nextButtonVisibility()