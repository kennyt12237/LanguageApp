from tkinter import Button, Misc
from tkinter import CENTER

from .DictionaryFrame import DictionaryFrame
from .GrammarFrame import GrammarFrame
from .SentenceFrame import SentenceFrame
from .AbstractFrame import GridFrame

from ..Window import Window
from ..Utils import convertPixelsToTextUnit


class SectionContentFrame(GridFrame):

    DICTIONARY = "dictionary"
    GRAMMAR = "grammar"
    SENTENCE = "sentence"
    WORDS = "words"
    GRAMMARS = "grammars"
    SENTENCES = "sentences"

    def __init__(self, master: Misc, sectionData=None, defaultWidgetSize: float = 0.1, **kwargs) -> None:
        super().__init__(master, **kwargs)
        self.window: Window = self.winfo_toplevel()
        self.data: dict[str, list[dict[str, str]]] = sectionData
        self.wordButton = Button(
            self, text=self.WORDS.capitalize(), command=lambda: self.onWordButtonPressed(self.data[self.WORDS]))
        self.grammarButton = Button(
            self, text=self.GRAMMARS.capitalize(), command=lambda: self.onGrammarButtonPressed(self.data[self.GRAMMARS]))
        self.sentenceButton = Button(
            self, text=self.SENTENCES.capitalize(), command=lambda: self.onSentenceButtonPressed(self.data[self.SENTENCES]))
        self.setAllButtonSizeRelativeToScreen(defaultWidgetSize)
        self._gridPlacement()

    def onWordButtonPressed(self, words: list[dict[str, str]]) -> None:
        self.window.newFrameNavigated(DictionaryFrame(
            self.window, words, name=self.DICTIONARY))

    def onGrammarButtonPressed(self, grammars: list[dict[str, str]]) -> None:
        self.window.newFrameNavigated(GrammarFrame(
            self.window, grammars, name=self.GRAMMAR))

    def onSentenceButtonPressed(self, sentences: list[dict[str, str]]) -> None:
        self.window.newFrameNavigated(SentenceFrame(
            self.window, sentences, name=self.SENTENCE))

    def setAllButtonSizeRelativeToScreen(self, relativeSize: float) -> None:
        widthSize = int(self.window.getWidth() * relativeSize)
        heightSize = int(self.window.getHeight() * relativeSize)
        for widget in self.winfo_children():
            if isinstance(widget, Button):
                widthUnit, heightUnit = convertPixelsToTextUnit(
                    widget, widthSize, heightSize)
                widget.configure(width=widthUnit, height=heightUnit)

    def _gridPlacement(self) -> None:
        self.wordButton.grid(row=0, column=0)
        self.grammarButton.grid(row=1, column=0)
        self.sentenceButton.grid(row=2, column=0)

    def _setGridProperties(self) -> None:
        self.grid_propagate(False)
        self.grid_anchor(CENTER)
