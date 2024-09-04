from tkinter import Frame, Button, Label, PhotoImage, Misc, Widget
from tkinter.ttk import Separator
from tkinter import N, S, E, W, CENTER, HORIZONTAL, SUNKEN, GROOVE
from enum import Enum

from .Section import GridFrame, Window
from .Section import sentenceMeaningFont, sentenceTextFont, stepLabelFont

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
        self.window.bindForFrameChange(self.onFrameChanged)
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


class MenuFrameWrapper(GridFrame):

    def __init__(self, master: Misc, **kwargs) -> None:
        super().__init__(master, **kwargs)
        self.menuFrame = MenuFrame(self, **kwargs)
        self.settingFrame = SettingFrame(
            self.winfo_toplevel(), borderwidth=3, relief="raised")
        self.settingFrame.setOnClosedButtonPressed(lambda: (self.settingFrame.place_forget(
        ), self.menuFrame.grid(row=0, column=0, sticky="nsew")))
        self.menuFrame.setOnSettingsButtonPressed(self.onSettingButtonPressed)
        self._gridPlacement()

    def setOnHomeButtonPressed(self, command) -> None:
        self.menuFrame.setOnHomeButtonPressed(command)

    def _setGridProperties(self) -> None:
        self.grid_propagate(False)

    def onSettingButtonPressed(self) -> None:
        self.settingFrame.lift()
        xPos = self.winfo_x()
        yPos = self.winfo_y()
        _, _, x2, _ = self.bbox()

        def onMenuFrameWrapperConfigure() -> None:
            xPos = self.winfo_x()
            yPos = self.winfo_y()
            self.settingFrame.place_configure(x=xPos, y=yPos)
        self.bind("<Configure>", lambda e: onMenuFrameWrapperConfigure())
        self.settingFrame.place(x=xPos, y=yPos, width=x2)

    def setOnSettingsButtonPressed(self, command) -> None:
        self.menuFrame.setOnSettingsButtonPressed(command)

    def _gridPlacement(self) -> None:
        self.menuFrame.grid(row=0, column=0, sticky="nsew")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        
    def hideButton(self, button: str) -> None:
        self.menuFrame.hideButton(button=button)

    def showButton(self, button: str) -> None:
        self.menuFrame.showButton(button=button)


class MenuFrame(GridFrame):

    HOME_PATH = os.path.join(
        os.getcwd(), 'src\App\View\Home\Icons', 'home.png')
    SETTINGS_PATH = os.path.join(
        os.getcwd(), 'src\App\View\Home\Icons', 'settings.png')

    HOME_BUTTON = "home"
    SETTING_BUTTON = "setting"

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
        self.homeImage = PhotoImage(file=self.HOME_PATH)
        self.settingsImage = PhotoImage(file=self.SETTINGS_PATH)
        self.homeButton = Button(self, name=self.HOME_BUTTON, image=self.homeImage)
        self.settingsButton = Button(
            self, name=self.SETTING_BUTTON, image=self.settingsImage, width=50)
        self.buttonDict: dict[str, Button] = {}
        self.buttonDict[self.HOME_BUTTON] = self.homeButton
        self.buttonDict[self.SETTING_BUTTON] = self.settingsButton
        self._gridPlacement()

    def _setGridProperties(self) -> None:
        self.grid_propagate(False)
        self.grid_anchor(CENTER)

    def _gridPlacement(self) -> None:
        ind = 0
        for widget in self.winfo_children():
            widget.grid(row=0, column=ind, sticky="nsew")
            self.grid_columnconfigure(ind, weight=1, minsize=100)
            ind += 1

    def _hideButton(self, button: str) -> None:
        b = self.buttonDict[button]
        if b in self.winfo_children():
            self.gridManager.removeWidget(b)

    def _showButton(self, button: str) -> None:
        b = self.buttonDict[button]
        if b in self.winfo_children():
            self.gridManager.retrieveWidget(b)

    def setOnSettingsButtonPressed(self, command) -> None:
        self.settingsButton.config(command=command)

    def setOnHomeButtonPressed(self, command) -> None:
        self.homeButton.config(command=command)

    def hideButton(self, button: str) -> None:
        self._hideButton(button=button)

    def showButton(self, button: str) -> None:
        self._showButton(button=button)


class SettingFrame(GridFrame):

    CLOSE = "Close"
    HEADER = "Setting"

    def __init__(self, master: Misc, **kwargs) -> None:
        super().__init__(master, **kwargs)
        self.header = Label(self, text=self.HEADER)
        self.sentenceSettingFrame = SentenceSettingFrame(self)
        self.closeButton = Button(self, text=self.CLOSE)
        self._gridPlacement()

    def setOnClosedButtonPressed(self, command) -> None:
        self.closeButton.config(command=command)

    def _gridPlacement(self) -> None:
        self.header.grid(row=0, column=0)
        self.sentenceSettingFrame.grid(row=1, column=0, pady=(0, 50))
        self.closeButton.grid(row=2, column=0, sticky=E)
        self.grid_columnconfigure(0, weight=1)


class SentenceSettingFrame(GridFrame):

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


class SizeFrame(GridFrame):

    SMALL = "Small"
    MEDIUM = "Medium"
    LARGE = "Large"

    def __init__(self, master: Misc, **kwargs) -> None:
        super().__init__(master, **kwargs)
        self.smallButton = Button(self, text=self.SMALL, relief=GROOVE)
        self.mediumButton = Button(self, text=self.MEDIUM, relief=SUNKEN)
        self.largeButton = Button(self, text=self.LARGE, relief=GROOVE)
        self._gridPlacement()

    def _setGridProperties(self) -> None:
        pass

    def _gridPlacement(self) -> None:
        self.smallButton.grid(row=0, column=0, sticky="nsew")
        self.mediumButton.grid(row=0, column=1, sticky="nsew")
        self.largeButton.grid(row=0, column=2, sticky="nsew")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)

    def __setButtonSunkenAndRaisedRest(self, button: Button) -> None:
        button.configure(relief=SUNKEN)
        for cButton in self.winfo_children():
            if cButton != button:
                cButton.configure(relief=GROOVE)

    def setOnSmallButtonPressed(self, command) -> None:
        self.smallButton.config(command=lambda: (
            command(), self.__setButtonSunkenAndRaisedRest(self.smallButton)))

    def setOnMediumButtonPressed(self, command) -> None:
        self.mediumButton.config(command=lambda: (
            command(), self.__setButtonSunkenAndRaisedRest(self.mediumButton)))

    def setOnLargeButtonPressed(self, command) -> None:
        self.largeButton.config(command=lambda: (
            command(), self.__setButtonSunkenAndRaisedRest(self.largeButton)))
