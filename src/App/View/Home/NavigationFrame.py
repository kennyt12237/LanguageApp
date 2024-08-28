from tkinter import Frame, Button, Label, PhotoImage, Misc, Widget
from tkinter import N, S, E, W, CENTER
from enum import Enum

from .Section import GridFrame, Window

import os


class NavigationFrame(GridFrame):

    class ButtonType(Enum):
        BACK = "back",
        HOME = "home",
        SETTINGS = "settings"

    ARROW_PATH = os.path.join(os.getcwd(), 'src\App\View\Home\Icons', 'arrow-left.png')
    HOME_PATH = os.path.join(os.getcwd(), 'src\App\View\Home\Icons', 'home.png')
    SETTINGS_PATH = os.path.join(os.getcwd(), 'src\App\View\Home\Icons', 'settings.png')

    def __init__(self, window: Window, **kwargs) -> None:
        super().__init__(window, **kwargs)
        self.window: Window = window
        self.backImage = PhotoImage(file=self.ARROW_PATH)
        self.homeImage = PhotoImage(file=self.HOME_PATH)
        self.settingsImage = PhotoImage(file=self.SETTINGS_PATH)
        self.window.bindForFrameChange(self.onFrameChanged)
        self.backButton = Button(self, image=self.backImage,
                                 command=self.backButtonPressed, width=50)
        self.frameLabel = Label(self, font=("Arial", 18), width=200)
        self.menuFrame = MenuFrame(self)
        self.menuButtonDict: dict[self.ButtonType,
                                  Button] = self._buttonDict(self.menuFrame)
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

    def settingButtonPressed(self) -> None:
        print("SettingButton Pressed")

    def _newFrameNavigated(self, nextFrame: Frame) -> None:
        self.__determineButtonChanges()
        self.__setFrameHeader(nextFrame)

    def __determineButtonChanges(self) -> None:
        if self.window.getNumberOfFramesNavigated() == 1:
            self.backButton.grid_forget()
            self.menuFrame.hideButton(
                self.menuButtonDict[self.ButtonType.HOME])
            return
        self.backButton.grid(row=0, column=0, sticky=W)
        self.menuFrame.showButton(self.menuButtonDict[self.ButtonType.HOME])

    def __setFrameHeader(self, frame: Frame) -> None:
        self.frameLabel.config(text=frame.winfo_name().capitalize())

    def _gridPlacement(self) -> None:
        self.frameLabel.grid(row=0, column=1, pady=50)
        self.menuFrame.grid(row=0, column=2, sticky="nsew")
        self.menuFrame.gridAllButtons()
        self.menuFrame.hideButton(self.menuButtonDict[self.ButtonType.HOME])
        self.columnconfigure(0, weight=1, minsize=200)
        self.columnconfigure(1, weight=4)
        self.columnconfigure(2, weight=1, minsize=200)
        self.rowconfigure(0, weight=1)

    def _setGridProperties(self) -> None:
        self.grid_propagate(False)

    def _buttonDict(self, parent) -> dict[ButtonType, Button]:
        buttonDict: dict[self.ButtonType, Button] = {}
        homeButton = Button(parent, image=self.homeImage,
                            command=self.homeButtonPressed)
        settingsButton = Button(
            parent, image=self.settingsImage, width=50, command=self.settingButtonPressed)

        buttonDict[self.ButtonType.HOME] = homeButton
        buttonDict[self.ButtonType.SETTINGS] = settingsButton
        return buttonDict


class MenuFrame(GridFrame):

    class RowStyle(Enum):
        ROW = "row",
        COLUMN = "column"

    class GridManager():

        def __init__(self) -> None:
            self.gridInfo = {}

        def removeWidget(self, widget: Widget) -> None:
            self.gridInfo[widget] = widget.grid_info()
            widget.grid_remove()

        def retrieveWidget(self, widget: Widget) -> None:
            if widget in self.gridInfo:
                previousGridInfo = self.gridInfo[widget]
                widget.grid(**previousGridInfo)

    def __init__(self, master: Misc = None, **kwargs) -> None:
        super().__init__(master, **kwargs)
        self.gridManager = self.GridManager()
        
    def _setGridProperties(self) -> None:
        self.grid_propagate(False)
        self.grid_anchor(CENTER)

    def _gridAllButtons(self, gridStyle: str = RowStyle.COLUMN) -> None:
        ind = 0
        for widget in self.winfo_children():
            if isinstance(widget, Button):
                if gridStyle == self.RowStyle.ROW:
                    widget.grid(row=ind, column=0)
                elif gridStyle == self.RowStyle.COLUMN:
                    widget.grid(row=0, column=ind, sticky="nsew")
                    self.grid_columnconfigure(ind, weight=1, minsize=100)
                ind += 1
            
    def _hideButton(self, button: Button) -> None:
        if button in self.winfo_children():
            self.gridManager.removeWidget(button)
        
    def _showButton(self, button: Button) -> None:
        if button in self.winfo_children():
            self.gridManager.retrieveWidget(button)

    def gridAllButtons(self, gridStyle: str = RowStyle.COLUMN) -> None:
        self._gridAllButtons(gridStyle=gridStyle)

    def hideButton(self, button: Button) -> None:
        self._hideButton(button=button)

    def showButton(self, button: Button) -> None:
        self._showButton(button=button)
