from tkinter import Frame, Button

from .DictionaryFrame import DictionaryFrame
from .GrammarFrame import GrammarFrame
from .SentenceFrame import SentenceFrame

from ..Window import Window

class SectionContentFrame(Frame):
    
    def __init__(self, window : Window, title : str, sectionData = None, name : str = "Section Content") -> None:
        super().__init__(window)
        self.window : Window = window
        self.name = name
        self.title : str = title
        self.data : dict[str,list[dict[str,str]]] = sectionData
        self.wordButton = Button(self, text="Words", command=lambda:self.onWordButtonPressed(self.data["words"]))
        self.grammarButton = Button(self, text="Grammars", command=lambda:self.onGrammarButtonPressed(self.data["grammars"]))
        self.sentenceButton = Button(self, text="Sentences", command=lambda:self.onSentenceButtonPressed(self.data["sentences"]))
        self.wordButton.grid(row=0, column=0)
        self.grammarButton.grid(row=1, column=0)
        self.sentenceButton.grid(row=2, column=0)
        
    def onWordButtonPressed(self, words : list[dict[str,str]]) -> None:
        self.window.newFrameNavigated(DictionaryFrame(self.window, words))

    def onGrammarButtonPressed(self, grammars : list[dict[str,str]]) -> None:
        self.window.newFrameNavigated(GrammarFrame(self.window, grammars))
        
    def onSentenceButtonPressed(self, sentences : list[dict[str,str]]) -> None:
        self.window.newFrameNavigated(SentenceFrame(self.window, sentences))
        
    def getName(self) -> None:
        return self.name