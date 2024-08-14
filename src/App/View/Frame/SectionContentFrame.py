from tkinter import Button, Misc
from tkinter import CENTER

from .DictionaryFrame import DictionaryFrame
from .GrammarFrame import GrammarFrame
from .SentenceFrame import SentenceFrame
from .GridFrame import GridFrame

from ..Window import Window
from ..Utils import convertPixelsToTextUnit

class SectionContentFrame(GridFrame):
    
    def __init__(self, master : Misc, sectionData = None, defaultWidgetSize : float = 0.1, name : str = "section content", **kwargs) -> None:
        kwargs["name"] = name
        super().__init__(master, **kwargs)
        self.window : Window = self.winfo_toplevel()
        self.defaultWidgetSize = defaultWidgetSize
        self.data : dict[str,list[dict[str,str]]] = sectionData
        self.wordButton = Button(self, text="Words", command=lambda:self.onWordButtonPressed(self.data["words"]))
        self.grammarButton = Button(self, text="Grammars", command=lambda:self.onGrammarButtonPressed(self.data["grammars"]))
        self.sentenceButton = Button(self, text="Sentences", command=lambda:self.onSentenceButtonPressed(self.data["sentences"]))
        self.wordButton.grid(row=0, column=0)
        self.grammarButton.grid(row=1, column=0)
        self.sentenceButton.grid(row=2, column=0)
        self._setButtonProperties()
        
    def onWordButtonPressed(self, words : list[dict[str,str]]) -> None:
        self.window.newFrameNavigated(DictionaryFrame(self.window, words))

    def onGrammarButtonPressed(self, grammars : list[dict[str,str]]) -> None:
        self.window.newFrameNavigated(GrammarFrame(self.window, grammars))
        
    def onSentenceButtonPressed(self, sentences : list[dict[str,str]]) -> None:
        self.window.newFrameNavigated(SentenceFrame(self.window, sentences))
        
    def _setButtonProperties(self) -> None:
        widthSize = int(self.window.getWidth() * self.defaultWidgetSize)
        heightSize = int(self.window.getHeight() * self.defaultWidgetSize)
        for widget in self.winfo_children():
            if isinstance(widget, Button):
                widthUnit, heightUnit = convertPixelsToTextUnit(widget, widthSize, heightSize)
                widget.configure(width=widthUnit, height=heightUnit)
            
    def _setGridProperties(self) -> None:
        self.grid_anchor(CENTER)
