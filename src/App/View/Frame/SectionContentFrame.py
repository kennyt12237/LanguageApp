from tkinter import Button, Misc

from .DictionaryFrame import DictionaryFrame
from .GrammarFrame import GrammarFrame
from .SentenceFrame import SentenceFrame
from .GridFrame import GridFrame

from ..Window import Window

class SectionContentFrame(GridFrame):
    
    def __init__(self, master : Misc, sectionData = None, name : str = "section content", **kwargs) -> None:
        kwargs["name"] = name
        super().__init__(master, **kwargs)
        self.window : Window = self.winfo_toplevel()
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