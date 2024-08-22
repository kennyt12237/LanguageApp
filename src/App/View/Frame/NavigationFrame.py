from tkinter import Frame, Button, Label, PhotoImage
from tkinter import W, E

from .AbstractFrame import GridFrame
from ..Window import Window

import os

class NavigationFrame(GridFrame):

    ARROW_PATH = os.path.join(os.getcwd(), 'src\App\Icons','arrow-left.png')
    HOME_PATH = os.path.join(os.getcwd(), 'src\App\Icons','home.png')
    
    def __init__(self, window: Window, **kwargs) -> None:
        super().__init__(window, **kwargs)
        self.window: Window = window
        self.backImage = PhotoImage(file=self.ARROW_PATH)
        self.homeImage = PhotoImage(file=self.HOME_PATH)
        self.window.bindForFrameChange(self.onFrameChanged)
        self.backButton = Button(self, image=self.backImage,
                                 command=self.backButtonPressed)
        self.frameLabel = Label(self, font=("Arial", 18))
        self.homeButton = Button(self, image=self.homeImage, command=self.homeButtonPressed)
        self._gridPlacement()
        self._setGridProperties()

    def setDefaultFrame(self, defaultFrame: Frame) -> None:
        self.__setFrameHeader(defaultFrame)

    def onFrameChanged(self, event) -> None:
        currentFrame = self.window.getCurrentFrame()
        self._newFrameNavigated(currentFrame)

    def backButtonPressed(self) -> None:
        self.window.returnToPreviousFrame()
        
    def homeButtonPressed(self) -> None:
        self.window.returnHome()

    def _newFrameNavigated(self, nextFrame: Frame) -> None:
        self.__determineButtonChanges()
        self.__setFrameHeader(nextFrame)

    def __determineButtonChanges(self) -> None:
        if self.window.getNumberOfFramesNavigated() == 1:
            self.backButton.grid_forget()
            self.homeButton.grid_forget()
            return
        self.backButton.grid(row=0, column=0, sticky=W)
        self.homeButton.grid(row=0, column=2, sticky=E)
        
    def __setFrameHeader(self, frame: Frame) -> None:
        self.frameLabel.config(text=frame.winfo_name().capitalize())

    def _gridPlacement(self) -> None:
        self.frameLabel.grid(row=0, column=1, pady=50)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=3)
        self.columnconfigure(2, weight=1)

    def _setGridProperties(self) -> None:
        self.grid_propagate(False)
