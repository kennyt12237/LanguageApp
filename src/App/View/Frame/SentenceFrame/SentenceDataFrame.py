from tkinter import Frame, Label, Misc
from tkinter import CENTER, LEFT, S, N, E, W, BOTTOM
from ..AbstractFrame import GridFrame

from ...Utils import getGrammarCharactersList, getGrammarDataFromCharacter
from ..Styling import getSentenceTextFont, getSentenceMeaningFont


class SentenceDataFrame(GridFrame):

    def __init__(self, rootFrame: Frame, sentence: str = None, meaning: str = None, grammarData: list[dict[str, str]] = None, **kwargs) -> None:
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
        self.sentenceFrame.grid(row=0, column=0, pady=(0, 40), sticky=N+S+E+W)
        self.meaningLabel.grid(row=1, column=0, sticky=N)

    def _setGridProperties(self) -> None:
        self.grid_anchor(CENTER)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)


class SentenceFrameWrapper(Frame):

    def __init__(self, master: Misc, text: str, font: tuple = None, grammarData: list[dict[str, str]] = None, **kwargs) -> None:
        super().__init__(master, **kwargs)
        self.sentenceFrame = SentenceFrame(
            self, text, font, grammarData, **kwargs)
        self.sentenceFrame.pack(side=BOTTOM)

    def changeLabels(self, text: str) -> None:
        self.sentenceFrame.changeLabels(text)


class SentenceFrame(Frame):

    BACKGROUND_COLOR = 'yellow'

    def __init__(self, master: Misc, text: str, font: tuple = None, grammarData: list[dict[str, str]] = None, **kwargs) -> None:
        super().__init__(master, **kwargs)
        self.font = font
        self.grammarData = grammarData
        self.characters: list[str] = getGrammarCharactersList(grammarData)
        self.changeLabels(text=text)

    def _createLabels(self, text: str) -> None:
        for char in text:
            if char in self.characters:
                label = LabelWithTooltip(self, tooltipParent=self.master, text=char, font=self.font,
                                         background=self.BACKGROUND_COLOR)
                grammar = getGrammarDataFromCharacter(self.grammarData, char)
                label.setToolTip(grammar=grammar)
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

    ENTER_SEQUENCE = "<Enter>"
    LEAVE_SEQUENCE = "<Leave>"

    def __init__(self, master: Misc, tooltipParent: Misc, **kwargs) -> None:
        super().__init__(master, **kwargs)
        self.tooltipParent = tooltipParent
        self.toolTip: Label = None

    def setToolTip(self, grammar: dict[str, str]) -> None:
        self.bind(self.ENTER_SEQUENCE, func=lambda e: self.__createTooltip(
            grammar))
        self.bind(self.LEAVE_SEQUENCE, func=lambda e: self.__removeToolTip())

    def __createTooltip(self, grammar: dict[str, str]) -> None:
        text = "Pinyin : {pinyin}\nCharacter : {character}{num}\nMeaning : {meaning}".format(
            pinyin=grammar["pinyin"],
            character=grammar["character"],
            num=grammar["number"],
            meaning=grammar["usage"])
        self.toolTip = Label(self.tooltipParent, text=text, borderwidth=2,
                             padx=10, pady=10, relief="solid", background="lightyellow")

        xPos = self.master.winfo_x() + self.winfo_x() - \
            (self.toolTip.winfo_reqwidth() / 2)
        yPos = self.tooltipParent.winfo_height() - self.master.winfo_height() - \
            self.toolTip.winfo_reqheight() - 20
        self.toolTip.place(x=xPos, y=yPos)

    def __removeToolTip(self) -> None:
        self.toolTip.destroy()
