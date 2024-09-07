from tkinter import Frame, Button, Label, PhotoImage
from tkinter import W
from enum import Enum

from ..Section import GridFrame, Window
from .Menu import MenuFrameWrapper, MenuFrame
import os


class NavigationFrame(GridFrame):

    class ButtonType(Enum):
        BACK = "back",
        HOME = "home",
        SETTINGS = "settings"

    ARROW_PATH = os.path.join(
        os.getcwd(), 'src\App\View\Home\Icons', 'arrow-left.png')

    def __init__(self, window: Window, **kwargs) -> None:
        super().__init__(window, **kwargs)
        self.window: Window = window
        self.backImage = PhotoImage(file=self.ARROW_PATH)
        self.bind_all("<<FrameChangeEvent>>", self.onFrameChanged)
        self.backButton = Button(self, image=self.backImage,
                                 command=self.backButtonPressed, width=50)
        self.frameLabel = Label(self, font=("Arial", 18), width=200)
        self.menuFrame = MenuFrameWrapper(self)
        self.menuFrame.setOnHomeButtonPressed(lambda: self.window.returnHome())

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
        self.__determineButtonChanges()
        self.__setFrameHeader(nextFrame)

    def __determineButtonChanges(self) -> None:
        if self.window.getNumberOfFramesNavigated() == 1:
            self.backButton.grid_forget()
            self.menuFrame.hideButton(MenuFrame.HOME_BUTTON)
            return
        self.backButton.grid(row=0, column=0, sticky=W)
        self.menuFrame.showButton(MenuFrame.HOME_BUTTON)

    def __setFrameHeader(self, frame: Frame) -> None:
        self.frameLabel.config(text=frame.winfo_name().capitalize())

    def _gridPlacement(self) -> None:
        self.frameLabel.grid(row=0, column=1, pady=50, sticky="nsew")
        self.menuFrame.grid(row=0, column=2, sticky="nsew")
        self.menuFrame.hideButton(MenuFrame.HOME_BUTTON)
        self.columnconfigure(0, weight=1, minsize=200)
        self.columnconfigure(1, weight=3)
        self.columnconfigure(2, weight=2, minsize=200)
        self.rowconfigure(0, weight=1)

    def _setGridProperties(self) -> None:
        self.grid_propagate(False)
