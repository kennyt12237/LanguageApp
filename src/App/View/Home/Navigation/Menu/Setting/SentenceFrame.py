from tkinter import Misc, Label
from tkinter.ttk import Separator
from tkinter import W, HORIZONTAL


from .SizeFrame import SizeFrame
from ....Section import Window, GridFrame
from ....Section import sentenceMeaningFont, sentenceTextFont, stepLabelFont

class SentenceFrame(GridFrame):

    SMALL_SIZE = 0.7
    MEDIUM_SIZE = 1.0
    LARGE_SIZE = 1.3

    def __init__(self, master: Misc, **kwargs) -> None:
        super().__init__(master, **kwargs)
        self.sentenceLabel = Label(
            self, text="Sentence", width=40, padx=4, anchor=W)
        self.seperator = Separator(self, orient=HORIZONTAL)
        self.sizeFrame = SizeFrame(self)
        self.sizeFrame.setOnSmallButtonPressed(
            lambda: self.onButtonPressed(self.SMALL_SIZE))
        self.sizeFrame.setOnMediumButtonPressed(
            lambda: self.onButtonPressed(self.MEDIUM_SIZE))
        self.sizeFrame.setOnLargeButtonPressed(
            lambda: self.onButtonPressed(self.LARGE_SIZE))
        self._gridPlacement()

    def onButtonPressed(self, multiplier: float) -> None:
        window: Window = self.winfo_toplevel()

        mFamily, mSize = sentenceMeaningFont
        meaningFont = (mFamily, int(mSize * multiplier))
        window.addWidgetStyling("meaningLabel", dict(font=meaningFont))

        textFamily, textSize = sentenceTextFont
        textFont = (textFamily, int(textSize * multiplier))
        window.addWidgetStyling("textLabel", dict(font=textFont))

        stepFamily, stepSize, stepWeight = stepLabelFont
        stepFont = (stepFamily, int(stepSize * multiplier), stepWeight)
        window.addWidgetStyling("stepLabel", dict(font=stepFont))

    def _gridPlacement(self) -> None:
        self.sentenceLabel.grid(row=0, column=0, sticky="nsew")
        self.seperator.grid(row=1, column=0, sticky="ew", pady=(0, 2))
        self.sizeFrame.grid(row=2, column=0, sticky="nsew")
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_columnconfigure(0, weight=1)
