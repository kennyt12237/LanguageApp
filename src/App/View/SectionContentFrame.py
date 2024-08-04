from tkinter import Frame, Button
from .WidgetUtils import packAllChildWidgets
from .DictionaryFrame import DictionaryFrame
from .GrammarFrame import GrammarFrame
from .Window import Window

class SectionContentFrame(Frame):
    
    def __init__(self, window : Window, title : str, sectionData = None) -> None:
        super().__init__(window)
        self.window : Window = window
        self.title : str = title
        self.data : dict[str,list[dict[str,str]]] = sectionData
        self.wordButton = Button(self, text="Words", command=lambda:self.onWordButtonPressed(self.data["words"]))
        self.grammarButton = Button(self, text="Grammars", command=lambda:self.onGrammarButtonPressed(self.data["grammars"]))
        self.sentenceButton = Button(self, text="Sentences")
        
    def onWordButtonPressed(self, words : list[dict[str,str]]) -> None:
        self.window.newFrameNavigated(DictionaryFrame(self.window, words))

    def onGrammarButtonPressed(self, grammars : list[dict[str,str]]) -> None:
        self.window.newFrameNavigated(GrammarFrame(self.window, grammars))
        
    def pack(self) -> None:
        packAllChildWidgets(self)
        super().pack()
        