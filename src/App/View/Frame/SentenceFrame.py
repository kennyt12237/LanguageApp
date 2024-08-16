from tkinter import Frame, Label, Button, Misc
from tkinter import CENTER, N, S, E, W
from typing import Callable
import json

from .Styling import getSentenceTextFont, getSentenceMeaningFont, getStepLabelFont
from .GridFrame import GridFrame

class SentenceFrame(GridFrame):
    
    def __init__(self, master : Misc, sentenceData : list[dict[str,str]] = None, initIndex : int = 0, name : str = "sentences", **kwargs) -> None:
        kwargs["name"] = name
        super().__init__(master, **kwargs)
        self.initIndex = initIndex
        self.sentenceData : list[dict[str,str]] = json.loads(sentenceData)
        self.sentenceDataFrame = SentenceDataFrame(self, self._getSentenceDataIndexSentence(self.initIndex), self._getSentenceDataIndexMeaning(self.initIndex))
        self.sentenceNavigationFrame = SentenceNavigationFrame(self, self.initIndex + 1, len(self.sentenceData), self.changeSentenceDataFrame)
        self.sentenceDataFrame.grid(row=0, column=0, sticky=N+S+E+W)
        self.sentenceNavigationFrame.grid(row=1, column=0, sticky=N+S+E+W)
        self.grid_rowconfigure(0, weight=11)
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)
        
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
    
class SentenceDataFrame(GridFrame):
    
    def __init__(self, rootFrame : Frame, sentence : str = None, meaning : str = None, **kwargs) -> None:
        super().__init__(rootFrame, **kwargs)
        self.rootFrame = rootFrame
        self.sentence = sentence
        self.meaning = meaning
        self.sentenceLabel = Label(self, text=sentence, font=getSentenceTextFont())
        self.meaningLabel = Label(self, text=meaning, font=getSentenceMeaningFont())
        
        self.sentenceLabel.grid(row=0, column=0, pady=(0,40))
        self.meaningLabel.grid(row=1, column=0)
        
    def changeLabelTexts(self, sentence : str = None, meaning : str = None) -> None:
        self.sentenceLabel.config(text=sentence)
        self.meaningLabel.config(text=meaning)
        
    def _setGridProperties(self) -> None:
        self.grid_anchor(CENTER)
        
class SentenceNavigationFrame(GridFrame):
    
    def __init__(self, rootFrame : Frame, initIndex : int = 1, totalSentences : int = 1, callback : Callable = None, **kwargs) -> None:
        super().__init__(rootFrame, **kwargs)
        self.rootFrame = rootFrame
        self.currentIndex = initIndex
        self.totalSentences = totalSentences
        self.callback = callback
        self.previousButton = Button(self, text="Previous", command=self._onPreviousButtonPressed)
        self.stepLabel = Label(self, text=self._regenerateStepLabelText(self.currentIndex, totalSentences), font=getStepLabelFont())
        self.nextButton = Button(self, text="Next", command=self._onNextButtonPressed)
        self.stepLabel.grid(row=0, column=1)
        self.grid_columnconfigure(0, weight = 1, minsize=100)
        self.grid_columnconfigure(1, weight = 10)
        self.grid_columnconfigure(2, weight = 1, minsize=100)
        self.grid_rowconfigure(0, weight=1)
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
            self.previousButton.grid_remove()
            return
        self.previousButton.grid(row=0, column=0, sticky=N+S+E+W)
        
    def __nextButtonVisibility(self) -> None:
        if self.currentIndex >= self.totalSentences:
            self.nextButton.grid_remove()
            return
        self.nextButton.grid(row=0, column=2, sticky=N+S+E+W)
            
    def _determineButtonVisibility(self) -> None:
        self.__previousButtonVisibility()
        self.__nextButtonVisibility()
        
    def _setGridProperties(self) -> None:
        self.grid_propagate(False)