from tkinter import Frame, Misc
from tkinter import CENTER, LEFT, S, N, E, W, BOTTOM, DISABLED
from tkinter.font import Font
from .KLabel import KLabel

from .Styling import sentenceTextFont, sentenceMeaningFont, dictionaryWordTooltipDefault, grammarTooltipDefault
from .Utils import TkManager, getGrammarCharactersList, getGrammarDataFromCharacter, getDictionaryCharactersList, getDictionaryDataFromCharacter

from ..AbstractFrame import GridFrame
from abc import ABC, abstractmethod


class SentenceDataFrame(GridFrame):

    MEANING_LABEL = "meaningLabel"

    def __init__(self, rootFrame: Frame, dictionaryData: list[dict[str, str]] = None, grammarData: list[dict[str, str]] = None, **kwargs) -> None:
        super().__init__(rootFrame, **kwargs)
        self.rootFrame = rootFrame
        self.grammarData = grammarData
        self.dictionaryData = dictionaryData
        self.sentenceFrame = SentenceFrameWrapper(
            self, font=Font(font=sentenceTextFont),  dictionaryData=self.dictionaryData, grammarData=self.grammarData)
        self.meaningLabel = KLabel(
            self, name=self.MEANING_LABEL, font=Font(font=sentenceMeaningFont))
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

    def __init__(self, master: Misc, font: Font = None,  dictionaryData: list[dict[str, str]] = None, grammarData: list[dict[str, str]] = None, tkManager: TkManager = None, **kwargs) -> None:
        super().__init__(master)
        self.sentenceFrame = SentenceFrame(
            self, font, dictionaryData, grammarData, tkManager, **kwargs)
        self.sentenceFrame.pack(side=BOTTOM)

    def changeLabels(self, text: str, manager: TkManager) -> None:
        self.sentenceFrame.changeLabels(text, manager)


class SentenceFrame(Frame):

    TEXT_LABEL = "textLabel"
    GRAMMAR_LABEL = "grammarLabel"
    WORD_LABEL = "wordLabel"
    GRAMMAR_LABEL_TOOLTIP = "gltooltip"
    WORD_LABEL_TOOLTIP = "wltooltip"
    CHAR_OFFSET = 2

    def __init__(self, master: Misc, font: Font = None,  dictionaryData: list[dict[str, str]] = None, grammarData: list[dict[str, str]] = None, manager: TkManager = None, **kwargs) -> None:
        super().__init__(master, **kwargs)
        self.font = font
        self.grammarData = grammarData
        self.dictionaryData = dictionaryData
        self.grammarChars: list[str] = getGrammarCharactersList(grammarData)
        self.dictionaryChars: list[str] = getDictionaryCharactersList(
            self.dictionaryData)

    def _createLabels(self, text: str) -> None:
        grammarTooltipGenerator = GrammarTooltipGenerator()
        wordTooltipGenerator = WordTooltipGenerator()
        textPos = 0
        while textPos < len(text):
            labelLength = 0
            labelName = self.TEXT_LABEL + str(len(self.winfo_children()))
            for gPos in range(0, len(self.grammarChars)):
                grammar = self.grammarChars[gPos]
                inTextAtPos = self.__findInText(text, grammar, textPos)
                if inTextAtPos == True:
                    label = grammarTooltipGenerator.createTooltipLabel(
                        master=self, tooltipParent=self.master, name=labelName + self.GRAMMAR_LABEL, text=grammar, font=self.font, **grammarTooltipDefault)
                    grammarData = getGrammarDataFromCharacter(
                        self.grammarData, grammar)
                    label.setToolTip(data=grammarData)
                    labelLength = len(grammar)
                    break
            if labelLength > 0:
                textPos += labelLength
                continue
            for dPos in range(0, len(self.dictionaryChars)):
                word = self.dictionaryChars[dPos]
                inTextAtPos = self.__findInText(text, word, textPos)
                if inTextAtPos == True:
                    label = wordTooltipGenerator.createTooltipLabel(
                        master=self, tooltipParent=self.master, name=labelName + self.WORD_LABEL, text=word, font=self.font, **dictionaryWordTooltipDefault)
                    wordData = getDictionaryDataFromCharacter(
                        self.dictionaryData, word)
                    label.setToolTip(data=wordData)
                    labelLength += len(word)
                    break
            if labelLength > 0:
                textPos += labelLength
                continue

            KLabel(self, text=text[textPos], name=labelName, font=self.font)
            textPos += 1

    def __findInText(self, text: str, sequence: str, textPos: int) -> bool:
        for sPos in range(len(sequence)):
            if textPos + sPos < len(text) and text[textPos + sPos] != sequence[sPos]:
                return False
        return True

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
            xPos += charWidth + self.CHAR_OFFSET
            label.bind("<<PropertyChange>>", lambda e,
                       label=label: self.onPropertyChange(e, label))
        self.config(width=xPos, height=self.font.metrics("linespace"))

    def _changeLabelPlacement(self, label: KLabel) -> None:

        labelList = self.winfo_children()
        labelInd = labelList.index(label)

        if labelInd == 0:
            self._changeLabelPlacement(labelList[labelInd + 1])
            return

        prevLabel = labelList[labelInd - 1]
        prevLabelFont = Font(font=prevLabel.cget("font"))
        prevxPos = int(prevLabel.place_info()['x'])
        prevLabelWidth = prevLabelFont.measure(prevLabel.cget('text'))
        newxPos = prevxPos + prevLabelWidth + self.CHAR_OFFSET
        label.place_configure(x=newxPos, y=0)

        if labelInd == len(labelList) - 1:
            currentLabelFont = Font(font=label.cget('font'))
            currentCharWidth = currentLabelFont.measure(label.cget('text'))
            newFrameWidth = newxPos + currentCharWidth + self.CHAR_OFFSET
            self.config(width=newFrameWidth,
                        height=currentLabelFont.metrics("linespace"))
        else:
            self._changeLabelPlacement(labelList[labelInd + 1])

    def onPropertyChange(self, event, label: KLabel) -> None:
        if self.winfo_children().index(label) == 0:
            self._changeLabelPlacement(label)

    def changeLabels(self, text: str, manager: TkManager = TkManager.PACK) -> None:
        self._removeAllLabels()
        self._createLabels(text=text)
        if manager == TkManager.PLACE:
            self._placeAllLabels()
        else:
            self._packAllLabels()


class LabelTooltip(ABC, KLabel):

    ENTER_SEQUENCE = "<Enter>"
    LEAVE_SEQUENCE = "<Leave>"

    def __init__(self, master: Misc, tooltipParent: Misc, tooltipName: str, **kwargs) -> None:
        super().__init__(master, **kwargs)
        self.tooltipParent = tooltipParent
        self.toolTip: KLabel = KLabel(self.tooltipParent, name=tooltipName, borderwidth=2,
                                      padx=10, pady=10, relief="solid", background="lightyellow")
        self.toolTip.event_generate(self.WIDGET_CREATED_EVENT)

    def setToolTip(self, data) -> None:
        self.bind(self.ENTER_SEQUENCE, func=lambda e: self.__setTooltipText(
            data))
        self.bind(self.LEAVE_SEQUENCE, func=lambda e: self.__hideToolTip())

    def __setTooltipText(self, data) -> None:
        self._setText(data)
        if self.toolTip.cget("state") != DISABLED:
            toolTipfont = Font(font=self.cget("font"))
            toolTipWidth = toolTipfont.measure(self.cget("text"))
            xPos = self.master.winfo_x() + self.winfo_x() + int(toolTipWidth / 2) - \
                (self.toolTip.winfo_reqwidth() / 2)
            yPos = self.tooltipParent.winfo_height() - self.master.winfo_height() - \
                self.toolTip.winfo_reqheight() - 20
            self.toolTip.place(x=xPos, y=yPos)

    @abstractmethod
    def _setText(self, data) -> KLabel:
        pass

    def __hideToolTip(self) -> None:
        self.toolTip.place_forget()


class GrammarLabelTooltip(LabelTooltip):

    def __init__(self, master: Misc, tooltipParent: Misc, tooltipName: str, **kwargs) -> None:
        super().__init__(master, tooltipParent, tooltipName, **kwargs)

    def _setText(self, data) -> None:
        text = "Pinyin : {pinyin}\nCharacter : {character}{num}\nMeaning : {meaning}".format(
            pinyin=data["pinyin"],
            character=data["character"],
            num=data["number"],
            meaning=data["usage"])
        self.toolTip.configure(text=text)


class DictionaryWordTooltip(LabelTooltip):

    def __init__(self, master: Misc, tooltipParent: Misc, **kwargs) -> None:
        super().__init__(master, tooltipParent, **kwargs)

    def _setText(self, data) -> None:
        text = "Pinyin : {pinyin}\nCharacter : {character}\nType : {type}\nMeaning : {meaning}".format(
            pinyin=data["pinyin"],
            character=data["character"],
            type=data["type"],
            meaning=data["meaning"])
        self.toolTip.configure(text=text)

class TooltipGenerator():

    DEFAULT_TOOLTIP_TEXT = "tooltip"

    def __init__(self, labelName: str = DEFAULT_TOOLTIP_TEXT, startingNumber: int = 0):
        self.labelName = labelName
        self.number = startingNumber

    def createTooltipLabel(self, master: Misc, tooltipParent: Misc, **kwargs) -> LabelTooltip:
        tooltipName = self.DEFAULT_TOOLTIP_TEXT + str(self.__getNumber())
        self.__incrementNumber()
        return self._createTooltipLabel(master, tooltipParent, tooltipName=tooltipName, **kwargs)

    def __incrementNumber(self) -> None:
        self.number += 1

    def __getNumber(self) -> int:
        return self.number

    def _createTooltipLabel(self, master: Misc, tooltipParent: Misc, tooltipName: str, **kwargs):
        return LabelTooltip(master, tooltipParent, tooltipName=tooltipName, **kwargs)
    
class WordTooltipGenerator(TooltipGenerator):
    
    WORD_LABEL_TOOLTIP = "wltooltip"
    
    def __init__(self, labelName : str = WORD_LABEL_TOOLTIP) -> None:
        super().__init__(labelName=labelName)
        
    def _createTooltipLabel(self, master: Misc, tooltipParent: Misc, tooltipName: str, **kwargs):
        return DictionaryWordTooltip(master, tooltipParent, tooltipName=tooltipName, **kwargs)
    
class GrammarTooltipGenerator(TooltipGenerator):
    
    GRAMMAR_LABEL_TOOLTIP = "gltooltip"
    
    def __init__(self, labelName : str = GRAMMAR_LABEL_TOOLTIP) -> None:
        super().__init__(labelName=labelName)
        
    def _createTooltipLabel(self, master: Misc, tooltipParent: Misc, tooltipName: str, **kwargs):
        return GrammarLabelTooltip(master, tooltipParent, tooltipName=tooltipName, **kwargs)