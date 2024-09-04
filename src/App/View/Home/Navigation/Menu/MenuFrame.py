from tkinter import Misc, Button, PhotoImage
from tkinter import CENTER

from ...Section import GridFrame

import os

class MenuFrame(GridFrame):

    HOME_PATH = os.path.join(
        os.getcwd(), 'src\App\View\Home\Icons', 'home.png')
    SETTINGS_PATH = os.path.join(
        os.getcwd(), 'src\App\View\Home\Icons', 'settings.png')

    HOME_BUTTON = "home"
    SETTING_BUTTON = "setting"

    def __init__(self, master: Misc = None, **kwargs) -> None:
        super().__init__(master, **kwargs)
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
            b.grid_remove()

    def _showButton(self, button: str) -> None:
        b = self.buttonDict[button]
        if b in self.winfo_children():
            b.grid()

    def setOnSettingsButtonPressed(self, command) -> None:
        self.settingsButton.config(command=command)

    def setOnHomeButtonPressed(self, command) -> None:
        self.homeButton.config(command=command)

    def hideButton(self, button: str) -> None:
        self._hideButton(button=button)

    def showButton(self, button: str) -> None:
        self._showButton(button=button)
