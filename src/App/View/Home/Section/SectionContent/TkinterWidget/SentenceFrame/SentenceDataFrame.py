from tkinter import Frame, Misc
from tkinter import CENTER, LEFT, S, N, E, W, BOTTOM
from tkinter.font import Font
from .KLabel import KLabel

from .Styling import getSentenceTextFont, getSentenceMeaningFont
from .Utils import TkManager, convertTupleToFont, getGrammarCharactersList, getGrammarDataFromCharacter

from ..AbstractFrame import GridFrame


class SentenceDataFrame(GridFrame):

    MEANING_LABEL = "meaningLabel"
    
    def __init__(self, rootFrame: Frame, grammarData: list[dict[str, str]] = None, **kwargs) -> None:
        super().__init__(rootFrame, **kwargs)
        self.rootFrame = rootFrame
        self.grammarData = grammarData
        self.sentenceFrame = SentenceFrameWrapper(
            self, font=convertTupleToFont(getSentenceTextFont()), grammarData=self.grammarData)
        self.meaningLabel = KLabel(
            self, name=self.MEANING_LABEL, font=convertTupleToFont(getSentenceMeaningFont()))
        self._gridPlacement()

    def changeLabelTexts(self, sentence: str = None, meaning: str = None, manager: TkManager = None) -> None:
        self.sentenceFrame.changeLabels(text=sentence, manager=manager)
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

    def __init__(self, master: Misc, font: Font = None, grammarData: list[dict[str, str]] = None, tkManager: TkManager = None, **kwargs) -> None:
        super().__init__(master)
        self.sentenceFrame = SentenceFrame(
            self, font, grammarData, tkManager, **kwargs)
        self.sentenceFrame.pack(side=BOTTOM)

    def changeLabels(self, text: str, manager: TkManager) -> None:
        self.sentenceFrame.changeLabels(text, manager)


class SentenceFrame(Frame):

    BACKGROUND_COLOR = 'yellow'
    TEXT_LABEL = "textLabel"

    def __init__(self, master: Misc, font: Font = None, grammarData: list[dict[str, str]] = None, manager: TkManager = None, **kwargs) -> None:
        super().__init__(master, **kwargs)
        self.font = font
        self.grammarData = grammarData
        self.config(background="red")
        self.characters: list[str] = getGrammarCharactersList(grammarData)
            
    def _createLabels(self, text: str) -> None:
        for char in text:
            labelName = self.TEXT_LABEL + str(len(self.winfo_children()))
            if char in self.characters:
                label = LabelWithTooltip(self, tooltipParent=self.master,  name=labelName, text=char, font=self.font,
                                         background=self.BACKGROUND_COLOR)
                grammar = getGrammarDataFromCharacter(self.grammarData, char)
                label.setToolTip(grammar=grammar)
            else:
                KLabel(self, text=char, name=labelName, font=self.font)

    def _removeAllLabels(self) -> None:
        for label in self.winfo_children():
            label.destroy()

    def _packAllLabels(self) -> None:
        for label in self.winfo_children():
            label.pack(side=LEFT, anchor=S)

    def _placeAllLabels(self) -> None:
        xPos = 0
        for label in self.winfo_children():
            label.place(x=xPos, y=0)
            charWidth = self.font.measure(label.cget("text"))
            xPos += charWidth + 2
            label.bind("<<PropertyChange>>", lambda e, label=label : self.onPropertyChange(e, label))
        self.config(width=xPos, height=self.font.metrics("linespace"))

    def onPropertyChange(self, event, label : KLabel) -> None:
        labelList = self.winfo_children()
        labelInd = labelList.index(label)
        if labelInd != 0:
            prevLabel = labelList[labelInd - 1]
            prevLabelPos = int(prevLabel.place_info()['x'])
            prevLabelFont = Font(font=prevLabel.cget('font'))
            prevCharWidth = prevLabelFont.measure(prevLabel.cget('text'))
            newxPos = prevLabelPos + prevCharWidth + 2
            label.place_configure(x = newxPos, y=0)
            if labelInd == len(labelList) - 1:
                currentLabelFont = Font(font=label.cget('font'))
                currentCharWidth = currentLabelFont.measure(label.cget('text'))
                newFrameWidth = newxPos + currentCharWidth + 2
                self.config(width=newFrameWidth, height=currentLabelFont.metrics("linespace"))
        
    def changeLabels(self, text: str, manager: TkManager = TkManager.PACK) -> None:
        self._removeAllLabels()
        self._createLabels(text=text)
        if manager == TkManager.PLACE:
            self._placeAllLabels()
        else:
            self._packAllLabels()


class LabelWithTooltip(KLabel):

    ENTER_SEQUENCE = "<Enter>"
    LEAVE_SEQUENCE = "<Leave>"

    def __init__(self, master: Misc, tooltipParent: Misc, **kwargs) -> None:
        super().__init__(master, **kwargs)
        self.tooltipParent = tooltipParent
        self.toolTip: KLabel = None

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
        self.toolTip = KLabel(self.tooltipParent, text=text, borderwidth=2,
                             padx=10, pady=10, relief="solid", background="lightyellow")

        xPos = self.master.winfo_x() + self.winfo_x() - \
            (self.toolTip.winfo_reqwidth() / 2)
        yPos = self.tooltipParent.winfo_height() - self.master.winfo_height() - \
            self.toolTip.winfo_reqheight() - 20
        self.toolTip.place(x=xPos, y=yPos)

    def __removeToolTip(self) -> None:
        self.toolTip.destroy()
