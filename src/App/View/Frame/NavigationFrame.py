from tkinter import Frame, Button, Label, W

from .AbstractFrame import GridFrame
from ..Window import Window


class NavigationFrame(GridFrame):

    BACK = '<-'

    def __init__(self, window: Window) -> None:
        super().__init__(window)
        self.window: Window = window
        self.window.bindForFrameChange(self.onFrameChanged)
        self.backButton = Button(self, text=self.BACK,
                                 command=self.backButtonPressed)
        self.frameLabel = Label(self, font=("Arial", 18))
        self._gridPlacement()
        self._setGridProperties()

    def setDefaultFrame(self, defaultFrame: Frame) -> None:
        self.__setFrameHeader(defaultFrame)

    def onFrameChanged(self, event) -> None:
        currentFrame = self.window.getCurrentFrame()
        self._newFrameNavigated(currentFrame)

    def backButtonPressed(self) -> None:
        self.window.returnToPreviousFrame()

    def _newFrameNavigated(self, nextFrame: Frame) -> None:
        self.__determineBackButtonChange()
        self.__setFrameHeader(nextFrame)

    def __determineBackButtonChange(self) -> None:
        if self.window.getNumberOfFramesNavigated() == 1:
            self.backButton.grid_forget()
            return
        self.backButton.grid(row=0, column=0, sticky=W)

    def __setFrameHeader(self, frame: Frame) -> None:
        self.frameLabel.config(text=frame.winfo_name().capitalize())

    def _gridPlacement(self) -> None:
        self.frameLabel.grid(row=0, column=1, pady=50, sticky=W)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)

    def _setGridProperties(self) -> None:
        self.grid_propagate(False)
